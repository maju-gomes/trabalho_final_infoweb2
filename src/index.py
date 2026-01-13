import streamlit as st
from templates import visualizarestoqueUI, visualizarusuariosUI, manterfavorecidoUI

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ['Visualizar Estoque', 'Visualizar Usuários', 'Cadastro de Favorecidos'])
        if op == 'Visualizar Estoque': visualizarestoqueUI.VEUI.main()
        if op == 'Visualizar Usuários': visualizarusuariosUI.VUUI.main()
        if op == 'Cadastro de Favorecidos': manterfavorecidoUI.MFUI.main()

IndexUI.main()