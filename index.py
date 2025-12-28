from model.usuarios import Doador
from view import DoadorView
from templates.manterdoadorUI import ManterDoadorUI
import streamlit as st


class IndexUI:
    def menu_doador():
        opcao = st.sidebar.selectbox("Menu",
            ["Meus Dados",
            "Propor Doação", 
            "Minhas Doações"])

        if opcao == "Meus Dados":
            PerfilDoadorUI.main()
        elif opcao == "Propor Doação":
            ProporDoacaoUI.main()
        elif opcao == "Minhas Doaões":
            ManterDoacaoUI.main()