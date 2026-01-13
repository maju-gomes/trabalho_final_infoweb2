import streamlit as st
import pandas as pd
from view import DoadorView, FavorecidoView, EnderecoView

class VUUI():
    def main():
        st.header("Visualizar Usuários")
        tab1, tab2 = st.tabs(["Doador", "Favorecido"])
        with tab1: VUUI.doadores()
        with tab2: VUUI.favorecidos()

    def doadores():
        doadores = DoadorView.listar()
        if not doadores:
            st.write('Nenhum doador cadastrado')
        else:
            list_dic = []
            for obj in doadores:
                list_dic.append(
                    {
                        'ID':obj.get_id(),
                        'Nome':obj.get_email(),
                        'CPF':obj.get_cpf(),
                        'Telefone':obj.get_telefone()
                    }
                )
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def favorecidos():
        favorecidos = FavorecidoView.listar()
        if not favorecidos:
            st.write('Nenhum favorecido cadastrado')
        else:
            list_dic = []
            for obj in favorecidos:
                e = EnderecoView.listar_id(obj.get_id_endereco())
                list_dic.append({
                        'ID':obj.get_id(),
                        'Nome':obj.get_nome(),
                        'CPF':obj.get_cpf(),
                        'Telefone':obj.get_telefone(),
                        'CEP':e.get_cep(),
                        'UF':e.get_uf(),
                        'Bairro':e.get_bairro(),
                        'Rua':e.get_rua(),
                        'Nº':e.get_numero(),
                        'Complemento':e.get_complemento()
                    })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)