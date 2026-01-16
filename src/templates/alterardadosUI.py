import streamlit as st
import time
from view import AdminView, DoadorView, FavorecidoView, EnderecoView

class PAUI:
    def main():
        st.header('Meus Dados')
        with st.form('upd_admin'):
            op = AdminView.listar_id(st.session_state['id_usuario'])
            nome = st.text_input('Informe o nome', op.get_nome())
            email = st.text_input('Informe o e-mail', op.get_email())
            senha = st.text_input('Informe a senha', op.get_senha(), type='password')
            cnpj = st.text_input('Informe o CNPJ', op.get_cnpj())
            submit = st.form_submit_button('Atualizar')
        if submit:
            try:
                id = op.get_id()
                AdminView.atualizar(id, nome, email, senha, cnpj)
                st.success('Dados atualizados com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

class PDUI:
    def main():
        st.header('Meus Dados')
        with st.form('upd_doador'):
            op = DoadorView.listar_id(st.session_state['id_usuario'])
            nome = st.text_input('Informe o nome', op.get_nome())
            email = st.text_input('Informe o e-mail', op.get_email())
            senha = st.text_input('Informe a senha', op.get_senha(), type='password')
            cpf = st.text_input('Informe o CPF', op.get_cpf())
            fone = st.text_input('Informe o telefone', op.get_telefone())
            submit = st.form_submit_button('Atualizar')
        if submit:
            try:
                id = op.get_id()
                DoadorView.atualizar(id, nome, email, senha, cpf, fone)
                st.success('Dados atualizados com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

class PFUI:
    def main():
        st.header('Meus Dados')
        with st.form('upd_fav'):
            op = FavorecidoView.listar_id(st.session_state['id_usuario'])
            end = EnderecoView.listar_id(op.get_id_endereco())
            with st.expander('Dados Pessoais', expanded=True):
                st.text_input('Informe o nome', op.get_nome(), disabled=True)
                st.text_input('Informe o e-mail', op.get_email(), disabled=True)
                st.text_input('Informe a senha', op.get_senha(), type='password', disabled=True)
                st.text_input('Informe o CPF', op.get_cpf(), disabled=True)
                st.text_input('Informe o telefone', op.get_telefone(), disabled=True)
            with st.expander('Dados de Endereço'):
                st.text_input('Informe o CEP', end.get_cep(), disabled=True)
                st.text_input('Informe a Unidade Federativa (UF)', end.get_uf(), disabled=True)
                st.text_input('Informe a cidade', end.get_cidade(), disabled=True)
                st.text_input('Informe o bairro', end.get_bairro(), disabled=True)
                st.text_input('Informe a rua', end.get_rua(), disabled=True)
                st.text_input('Informe o número', end.get_numero(), disabled=True)
                st.text_input('Informe o complemento', end.get_complemento(), disabled=True)
        st.write('Atualização de dados apenas em nossas agências de cadastro de favorecidos')