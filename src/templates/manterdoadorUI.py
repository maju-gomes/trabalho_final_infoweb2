from view import DoadorView
import streamlit as st
import pandas as pd
import time

class ManterDoadorUI:
    def main():
        st.header("Cadastro de Doadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterDoadorUI.listar()
        with tab2: ManterDoadorUI.inserir()
        with tab3: ManterDoadorUI.atualizar()
        with tab4: ManterDoadorUI.excluir()

    def listar():
        doadores = DoadorView.listar_doador()
        if len(doadores) == 0:
            st.write("Nenhum doador cadastrado")
        else:
            colunas = ["id", "nome", "e-mail", "senha", "cpf", "tel"]
            df = pd.DataFrame(doadores, columns=colunas)
            st.dataframe(df)


ManterDoadorUI.main()