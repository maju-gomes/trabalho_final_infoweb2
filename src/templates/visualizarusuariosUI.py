import streamlit as st
import pandas as pd
from view import DoadorView, FavorecidoView, EnderecoView, DoacaoView

class VUUI:
    def main():
        st.header('Visualizar Usuários')
        tab1, tab2 = st.tabs(['Favorecidos', 'Doadores'])
        with tab1: VUUI.favorecidos()
        with tab2: VUUI.doadores()

    def favorecidos():
        fav = FavorecidoView.listar()
        if not fav:
            st.write('Nenhum favorecido cadastrado')
        else:
            list_dic = []
            for obj in fav:
                e = EnderecoView.listar_id(obj.get_id_endereco())
                cpf = f"{obj.get_cpf()[:3]}.{obj.get_cpf()[3:6]}.{obj.get_cpf()[6:9]}-{obj.get_cpf()[9:11]}"
                end = f"{e.get_rua()}, {e.get_numero()} - {e.get_bairro()}, {e.get_cidade()}/{e.get_uf()}"
                list_dic.append({
                    'Titular':f"{obj.get_nome()} ({cpf})",
                    'E-mail':obj.get_email(),
                    'Telefone':obj.get_telefone(),
                    'CEP':e.get_cep(),
                    'Endereço':end,
                    'Complemento':e.get_complemento()
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def doadores():
        do = DoadorView.listar()
        if not do:
            st.write('Nenhum doador cadastrado')
        else:
            list_dic = []
            for obj in do:
                cpf = f"{obj.get_cpf()[:3]}.{obj.get_cpf()[3:6]}.{obj.get_cpf()[6:9]}-{obj.get_cpf()[9:11]}"
                doacoes = sum(1 for d in DoacaoView.listar() if d.get_id_doador() == obj.get_id())
                list_dic.append({
                    'Titular':f"{obj.get_nome()} ({cpf})",
                    'E-mail':obj.get_email(),
                    'Telefone':obj.get_telefone(),
                    'Doações':doacoes
                })
            df = pd.DataFrame(list_dic)
            st.dataframde(df)