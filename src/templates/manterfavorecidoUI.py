import streamlit as st
import time
from view import FavorecidoView, EnderecoView

class MFUI:
    def main():
        st.header('Cadastro de Favorecidos')
        tab1, tab2, tab3 = st.tabs(['Inserir', 'Atualizar', 'Excluir'])
        with tab1: MFUI.inserir()
        with tab2: MFUI.atualizar()
        with tab3: MFUI.excluir()

    def inserir():
        with st.form('ins_favorecido'):
            with st.expander('Dados Favorecido', expanded=True):
                nome = st.text_input('Informe o nome', key='ins_fav_nome')
                email = st.text_input('Informe o e-mail', key='ins_fav_email')
                senha = st.text_input('Informe a senha', key='ins_fav_senha', type='password')
                cpf = st.text_input('Informe o CPF', key='ins_fav_cpf')
                tel = st.text_input('Informe o telefone', key='ins_fav_tel')
            with st.expander('Endereço'):
                cep = st.text_input('Informe o CEP', key='ins_cep')
                uf = st.text_input('Informe a Unidade Federativa', key='ins_uf')
                cidade = st.text_input('Informe a cidade', key='ins_cidade')
                bairro = st.text_input('Informe o bairro', key='ins_bairro')
                rua = st.text_input('Informe a rua', key='ins_rua')
                num = st.text_input('Informe o número', key='ins_numero')
                com = st.text_input('Informe o complemento', key='ins_complemento')
            submit = st.form_submit_button('Cadastrar')
        if submit:
            try:
                i_e = EnderecoView.inserir(cep, uf, cidade, bairro, rua, num, com)
                FavorecidoView.inserir(nome, email, senha, cpf, tel, i_e)
                st.success('Favorecido cadastrado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        fav = [f.get_id() for f in FavorecidoView.listar()]
        if not fav:
            st.write('Nenhum favorecido cadastrado')
        else:
            with st.form('upd_favorecido'):
                op = st.selectbox(
                    'Atualização de Favorecidos',
                    fav,
                    format_func=lambda id:f'{FavorecidoView.listar_id(id).get_nome()} - {FavorecidoView.listar_id(id).get_cpf()}',
                    key='upd_select_fav'
                    )
                obj = FavorecidoView.listar_id(op)
                end = EnderecoView.listar_id(obj.get_id_endereco())
                with st.expander('Dados Favorecido', expanded=True):
                    nome = st.text_input('Informe o nome', obj.get_nome(), key='upd_fav_nome')
                    email = st.text_input('Informe o e-mail', obj.get_email(), key='upd_fav_email')
                    senha = st.text_input('Informe a senha', obj.get_senha(), key='upd_fav_senha', type='password')
                    cpf = st.text_input('Informe o CPF', obj.get_cpf(), key='upd_fav_cpf')
                    tel = st.text_input('Informe o telefone', obj.get_telefone(), key='upd_fav_tel')
                with st.expander('Endereço'):
                    cep = st.text_input('Informe o CEP', end.get_cep(), key='upd_cep')
                    uf = st.text_input('Informe a Unidade Federativa', end.get_uf(), key='upd_uf')
                    cidade = st.text_input('Informe a cidade', end.get_cidade(), key='upd_cidade')
                    bairro = st.text_input('Informe o bairro', end.get_bairro(), key='upd_bairro')
                    rua = st.text_input('Informe a rua', end.get_rua(), key='upd_rua')
                    num = st.text_input('Informe o número', end.get_numero(), key='upd_numero')
                    com = st.text_input('Informe o complemento', end.get_complemento(), key='upd_complemento')
                submit = st.form_submit_button('Atualizar')
            if submit:
                try:
                    i_e = EnderecoView.atualizar(end.get_id(), cep, uf, cidade, bairro, rua, num, com)
                    FavorecidoView.atualizar(op.get_id(), nome, email, senha, cpf, tel, i_e)
                    st.success('Favorecido atualizado com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        fav = [f.get_id() for f in FavorecidoView.listar()]
        if not fav:
            st.write('Nenhum favorecido cadastrado')
        else:
            op = st.selectbox(
                'Exclusão de Favorecidos',
                fav,
                format_func=lambda id:f'{FavorecidoView.listar_id(id).get_nome()} - {FavorecidoView.listar_id(id).get_cpf()}',
                key='del_select_fav'
                )
            if st.button('Excluir'):
                try:
                    obj = FavorecidoView.listar_id(op)
                    i_e = obj.get_id_endereco()
                    FavorecidoView.excluir(op)
                    EnderecoView.excluir(i_e)
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()