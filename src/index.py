import streamlit as st
from view import DoadorView, FavorecidoView
from templates import autenticarUI, manterfavorecidoUI, visualizarusuariosUI, reciclagemUI, alterardadosUI, manterdoacaoUI, manterprodutoUI

class IndexUI:
    def main():
        IndexUI.sidebar()
        
    def menu_visitante():
        if 'liberar_admin' not in st.session_state:
            st.session_state.liberar_admin = False

        op = st.sidebar.selectbox('Menu', ['Entrar no Sistema', 'Criar Conta', 'Cadastro de Administrador'])
        if op == 'Entrar no Sistema':
            st.session_state.liberar_admin = False
            autenticarUI.FLUI.main()
        if op == 'Criar Conta':
            st.session_state.liberar_admin = False
            autenticarUI.CCUI.main()
        if op == 'Cadastro de Administrador': autenticarUI.CAUI.main()

    def menu_admin():
        if 'liberar_fav' not in st.session_state:
            st.session_state.liberar_fav = False

        op = st.sidebar.selectbox('Menu', ['Cadastro de Favorecidos', 'Visualizar Usuários', 'Registrar Reciclagem', 'Atualizar Dados'])
        if op == 'Cadastro de Favorecidos': manterfavorecidoUI.MFUI.main()
        if op == 'Visualizar Usuários':
            st.session_state.liberar_fav = False
            visualizarusuariosUI.VUUI.main()
        if op == 'Registrar Reciclagem':
            st.session_state.liberar_fav = False
            reciclagemUI.RUI.main()
        if op == 'Atualizar Dados':
            st.session_state.liberar_fav = False
            alterardadosUI.PAUI.main()

    def menu_doador():
        op = st.sidebar.selectbox('Menu', ['Cadastro de Doações', 'Atualizar Dados'])
        if op == 'Cadastro de Doações': manterdoacaoUI.MDUI.main()
        if op == 'Atualizar Dados': alterardadosUI.PDUI.main()

    def menu_favorecido():
        op = st.sidebar.selectbox('Menu', ['Meus Produtos', 'Visualizar Dados'])
        if op == 'Meus Produtos': manterprodutoUI.MPUI.main()
        if op == 'Visualizar Dados': alterardadosUI.PFUI.main()

    def sair_sistema():
        if st.sidebar.button('Sair'):
            del st.session_state['id_usuario']
            del st.session_state['nome_usuario']
            st.rerun()
    
    def sidebar():
        if 'id_usuario' not in st.session_state:
            IndexUI.menu_visitante()
        else:
            nome_user = st.session_state['nome_usuario']
            id_user = st.session_state['id_usuario']
            st.sidebar.write('Bem-vindo(a), ' + nome_user)
            if id_user in [obj.get_id() for obj in DoadorView.listar()]:
                IndexUI.menu_doador()
            elif id_user in [obj.get_id() for obj in FavorecidoView.listar()]:
                IndexUI.menu_favorecido()
            else:
                IndexUI.menu_admin()
            IndexUI.sair_sistema()

IndexUI.main()