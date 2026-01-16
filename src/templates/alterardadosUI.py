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
            cnpj_old = f"{op.get_cnpj()[:2]}.{op.get_cnpj()[2:5]}.{op.get_cnpj()[5:8]}/{op.get_cnpj()[8:12]}-{12:}"
            cnpj = st.text_input('Informe o CNPJ', cnpj_old)
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
            cpf_old = f"{op.get_cpf()[:3]}.{op.get_cpf()[3:6]}.{op.get_cpf()[6:9]}-{op.get_cpf()[9:]}"
            cpf = st.text_input('Informe o CPF', cpf_old)
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
        st.warning('Atualização de dados apenas em nossas agências de cadastro de favorecidos')
        op = FavorecidoView.listar_id(st.session_state['id_usuario'])
        end = EnderecoView.listar_id(op.get_id_endereco())
        with st.expander('Dados Pessoais', expanded=True):
            st.text_input('Nome', op.get_nome(), disabled=True)
            st.text_input('E-mail', op.get_email(), disabled=True)
            st.text_input('Senha', op.get_senha(), type='password', disabled=True)
            cpf_old = f"{op.get_cpf()[:3]}.{op.get_cpf()[3:6]}.{op.get_cpf()[6:9]}-{op.get_cpf()[9:]}"
            st.text_input('CPF', cpf_old, disabled=True)
            st.text_input('Telefone', op.get_telefone(), disabled=True)
        with st.expander('Dados de Endereço'):
            st.text_input('CEP', end.get_cep(), disabled=True)
            st.text_input('Unidade Federativa (UF)', end.get_uf(), disabled=True)
            st.text_input('Cidade', end.get_cidade(), disabled=True)
            st.text_input('Bairro', end.get_bairro(), disabled=True)
            st.text_input('Rua', end.get_rua(), disabled=True)
            st.text_input('Número', end.get_numero(), disabled=True)
            st.text_input('Complemento', end.get_complemento(), disabled=True)