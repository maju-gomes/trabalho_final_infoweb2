import streamlit as st
import time
from view import AdminView, FavorecidoView, DoadorView

class FLUI:
    def main():
        st.header('Entrar no Sistema')
        with st.form('entrar_sistema'):
            email_cnpj = st.text_input('Informe o e-mail ou CPF/CNPJ', key='login_email_cnpj')
            senha = st.text_input('Informe a senha', key='login_senha', type='password')
            submit = st.form_submit_button('Entrar')
            if submit:
                user = AdminView.autenticar(email_cnpj, senha) or DoadorView.autenticar(email_cnpj, senha) or FavorecidoView.autenticar(email_cnpj, senha)
                if user:
                    st.session_state['id_usuario'] = user.get_id()
                    st.session_state['nome_usuario'] = user.get_nome()
                    st.rerun()
                else:
                    st.write('E-mail ou senha inválidos')

class CCUI:
    def main():
        st.header('Criar Conta no Sistema')
        with st.form('criar_conta'):
            nome = st.text_input('Informe o nome', key='doador_nome')
            email = st.text_input('Informe o e-mail', key='doador_email')
            senha = st.text_input('Informe a senha', key='doador_senha', type='password')
            cpf = st.text_input('Informe o CPF')
            fone = st.text_input('Informe o telefone')
            submit = st.form_submit_button('Registar-se')
            if submit:
                try:
                    DoadorView.inserir(nome, email, senha, cpf, fone)
                    st.success('Conta criada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

class CAUI:
    def main():
        st.header('Cadastro de Administrador')
        if not st.session_state.liberar_admin:
            with st.form('autorizar_admin'):
                senha_form = st.text_input('Informe a senha', key='senha_form', type='password')
                entrar = st.form_submit_button('Entrar')
                if entrar:
                    if senha_form == 'infoweb2024':
                        st.session_state.liberar_admin = True
                        st.rerun()
                    else:
                        st.write('Senha Inválida')
        else:
            with st.form('ins_admin'):
                nome = st.text_input('Informe o nome', key='admin_nome')
                email = st.text_input('Informe o e-mail', key='admin_email')
                senha = st.text_input('Informe a senha', key='admin_senha', type='password')
                cnpj = st.text_input('Informe o CNPJ')
                submit = st.form_submit_button('Registrar-se')
                if submit:
                    try:
                        AdminView.inserir(nome, email, senha, cnpj)
                        st.session_state.liberar_admin = False
                        st.success('Conta criada com sucesso')
                    except ValueError as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()