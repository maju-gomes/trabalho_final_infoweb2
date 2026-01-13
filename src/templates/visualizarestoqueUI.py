import streamlit as st
import pandas as pd
from view import DoacaoView, ProdutoView

class VEUI():
    def main():
        st.header('Visualizar Estoque')
        tab1, tab2 = st.tabs(['Doações', 'Produtos'])
        with tab1: VEUI.doacoes()
        with tab2: VEUI.produtos()

    def doacoes():
        doacoes = [d for d in DoacaoView.listar() if d.get_situacao() == None]
        if not doacoes:
            st.write('Nenhuma doação em estoque')
        else:
            d = {}
            list_dic = []
            id = 1
            for obj in doacoes:
                chave = (obj.get_descricao(), obj.get_tipo())
                d[chave] = d.get(chave, 0) + obj.get_quantidade_disponivel()
            for (desc, tipo), qntd in d.items():
                list_dic.append({
                    'ID':id,
                    'Descrição':desc,
                    'Tipo':tipo,
                    'Quantidade':qntd
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def produtos():
        produtos = [p for p in ProdutoView.listar() if p.get_id_favorecido() == None]
        if not produtos:
            st.write('Nenhum produto em estoque')
        else:
            p = {}
            list_dic = []
            id = 1
            for obj in produtos:
                chave = (obj.get_descricao(), obj.get_tipo())
                p[chave] = p.get(chave, 0) + obj.get_quantidade()
            for (desc, tipo), qntd in p.items():
                list_dic.append({
                    'ID':id,
                    'Descrição':desc,
                    'Tipo':tipo,
                    'Quantidade':qntd
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)