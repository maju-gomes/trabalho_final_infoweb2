import streamlit as st
from dao.database import Database
from view import DoadorView, FavorecidoView, AdminView
from templates import autenticarUI, manterfavorecidoUI, visualizarusuariosUI, reciclagemUI, confirmarUI, alterardadosUI, manterdoacaoUI, manterprodutoUI

class IndexUI:
    def main():
        Database.abrir()
        Database.criar_tabelas()
        Database.fechar()        
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

        op = st.sidebar.selectbox('Menu', ['Registrar Reciclagem', 'Confirmar Doação', 'Visualizar Usuários', 'Cadastro de Favorecidos', 'Atualizar Dados'])
        if op == 'Registrar Reciclagem':
            st.session_state.liberar_fav = False
            reciclagemUI.RUI.main()
        if op == 'Confirmar Doação':
            st.session_state.liberar_fav = False
            confirmarUI.CDUI.main()
        if op == 'Visualizar Usuários':
            st.session_state.liberar_fav = False
            visualizarusuariosUI.VUUI.main()
        if op == 'Cadastro de Favorecidos':
            manterfavorecidoUI.MFUI.main()
        if op == 'Atualizar Dados':
            st.session_state.liberar_fav = False
            alterardadosUI.PAUI.main()

    def menu_doador():
        op = st.sidebar.selectbox('Menu', ['Cadastro de Doações', 'Atualizar Dados'])
        if op == 'Cadastro de Doações': manterdoacaoUI.MDUI.main()
        if op == 'Atualizar Dados': alterardadosUI.PDUI.main()

    def menu_favorecido():
        op = st.sidebar.selectbox('Menu', ['Meus Produtos', 'Confirmar Recebimento' ,'Visualizar Dados'])
        if op == 'Meus Produtos': manterprodutoUI.MPUI.main()
        if op == 'Confirmar Recebimento': confirmarUI.CPUI.main()
        if op == 'Visualizar Dados': alterardadosUI.PFUI.main()

    def deletar_conta():
        if 'confirmar' not in st.session_state:
            st.session_state.confirmar = False
        if not st.session_state.confirmar:
            if st.sidebar.button('Deletar Conta'):
                st.session_state.confirmar = True
                st.rerun()
        else:
            with st.sidebar.container(border=True):
                st.warning('Tem certeza que deseja deletar sua conta?')
                st.caption('Essa ação não pode ser desfeita.')
                col1, col2 = st.columns(2)
                if col1.button('Deletar'):
                    try:
                        id_user = st.session_state['id_usuario']
                        if DoadorView.listar_id(id_user):
                            DoadorView.excluir(id_user)
                        elif AdminView.listar_id(id_user):
                            AdminView.excluir(id_user)
                        st.session_state.confirmar = False
                        IndexUI.sair_sistema()
                    except ValueError as erro:
                        st.error(erro)
                if col2.button('Cancelar'):
                    st.session_state.confirmar = False
                    st.rerun()
        
    def sair_sistema():
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
            if AdminView.listar_id(id_user):
                IndexUI.menu_admin()
                IndexUI.deletar_conta()
            elif DoadorView.listar_id(id_user):
                IndexUI.menu_doador()
                IndexUI.deletar_conta()
            else:
                IndexUI.menu_favorecido()
            if st.sidebar.button('Sair'):
                IndexUI.sair_sistema()

IndexUI.main()