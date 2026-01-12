import streamlit as st
import pandas as pd
import time
from view import UsuarioView, AdminView, FavorecidoView, DoadorView, DoacaoView, ProdutoView

class ManterDoadorUI:
    def main():
        st.header("Cadastro de Doador")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterDoadorUI.listar()
        with tab2: ManterDoadorUI.inserir()
        with tab3: ManterDoadorUI.atualizar()
        with tab4: ManterDoadorUI.excluir()

    def listar():
        doadores = DoadorView.listar()
        if len(doadores) == 0:
            st.write("Nenhum doador cadastrado")
        else:
            df = pd.DataFrame(doadores)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Digite seu nome"),
        email = st.text_input("Digite seu email:"),
        senha = st.text_input("Insira sua senha:", type="password"),
        telefone = st.text_input("Digite seu telefone"),
        cpf = st.text_input("Digite seu CPF:")

        if st.button("Inserir"):
            DoadorView.inserir(nome, email, senha, cpf, telefone)
            st.sucess("Doador inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        pass
    def exluir():
        pass
        
