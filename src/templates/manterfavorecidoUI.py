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
        st.session_state.liberar_fav = False
        with st.form('ins_fav'):
            with st.expander('Dados Pessoais', expanded=True):
                nome = st.text_input('Informe o nome', key='ins_fav_nome')
                email = st.text_input('Informe o e-mail', key='ins_fav_email')
                senha = st.text_input('Informe a senha', key='ins_fav_senha', type='password')
                cpf = st.text_input('Informe o CPF', key='ins_fav_cpf')
                fone = st.text_input('Informe o telefone', key='ins_fav_fone')
            with st.expander('Dados de Endereço'):
                cep = st.text_input('Informe o CEP', key='ins_fav_cep')
                uf = st.text_input('Informe a Unidade Federativa (UF)', key='ins_fav_uf')
                ci = st.text_input('Informe a cidade', key='ins_fav_cidade')
                ba = st.text_input('Informe o bairro', key='ins_fav_bairro')
                rua = st.text_input('Informe a rua', key='ins_fav_rua')
                num = st.text_input('Informe o número', key='ins_fav_num')
                com = st.text_input('Informe o complemento', key='ins_fav_com')
            submit = st.form_submit_button('Cadastrar')
        if submit:
            try:
                i_e = EnderecoView.inserir(cep, uf, ci, ba, rua, num, com)
                FavorecidoView.inserir(nome, email, senha, cpf, fone, i_e)
                st.success('Favorecido cadastrado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        if not st.session_state.liberar_fav:
            with st.form('autorizar_upd'):
                email_cpf = st.text_input('Informe o e-mail ou CPF')
                senha_aut = st.text_input('Informe a senha', key='senha_aut')
                submit = st.form_submit_button('Entrar')
            if submit:
                op = FavorecidoView.autenticar(email_cpf, senha_aut)
                if not op:
                    st.write('Dados Inválidos')
                else:
                    st.session_state.liberar_fav = True
                    st.rerun()
        else:
            with st.form('ins_fav'):
                end = EnderecoView.listar_id(op.get_id_endereco())
                with st.expander('Dados Pessoais', expanded=True):
                    nome = st.text_input('Informe o nome', op.get_nome(), key='upd_fav_nome')
                    email = st.text_input('Informe o e-mail', op.get_email(), key='upd_fav_email')
                    senha = st.text_input('Informe a senha', op.get_senha(), key='upd_fav_senha', type='password')
                    cpf = st.text_input('Informe o CPF', op.get_cpf(), key='upd_fav_cpf')
                    fone = st.text_input('Informe o telefone', op.get_telefone(), key='upd_fav_fone')
                with st.expander('Dados de Endereço'):
                    cep = st.text_input('Informe o CEP', end.get_cep(), key='upd_fav_cep')
                    uf = st.text_input('Informe a Unidade Federativa (UF)', end.get_uf(), key='upd_fav_uf')
                    ci = st.text_input('Informe a cidade', end.get_cidade(), key='upd_fav_cidade')
                    ba = st.text_input('Informe o bairro', end.get_bairro(), key='upd_fav_bairro')
                    rua = st.text_input('Informe a rua', end.get_rua(), key='upd_fav_rua')
                    num = st.text_input('Informe o número', end.get_numero(), key='upd_fav_num')
                    com = st.text_input('Informe o complemento', end.get_complemento(), key='upd_fav_com')
                submit = st.form_submit_button('Atualizar')
            if submit:
                try:
                    i_e = EnderecoView.atualizar(cep, uf, ci, ba, rua, num, com)
                    FavorecidoView.atualizar(op.get_id(), nome, email, senha, cpf, fone, i_e)
                    st.session_state.liberar_fav = False
                    st.success('Dados atualizados com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        with st.form('autorizar_del'):
            email_cpf = st.text_input('Informe o e-mail ou CPF')
            senha_aut = st.text_input('Informe a senha', key='senha_aut')
            submit = st.form_submit_button('Deletar')
        if submit:
            op = FavorecidoView.autenticar(email_cpf, senha_aut)
            if not op:
                st.write('Dados Inválidos')
            else:
                try:
                    FavorecidoView.excluir(op.get_id())
                    st.success('Favorecido excluído com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()