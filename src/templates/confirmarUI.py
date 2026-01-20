import streamlit as st
import time
from view.view import DoacaoView, ProdutoView, DoadorView

class CDUI:
    def main():
        st.header('Confirmar Doação')
        doacoes = [d for d in DoacaoView.listar() if d.get_situacao() == 'Pendente']
        if not doacoes:
            st.write('Nenhuma doação pendente')
            return
        with st.form('conf_doacao'):
            opcoes, mapa = [], []
            for d in doacoes:
                doador = DoadorView.listar_id(d.get_id_doador())
                cpf = f"{doador.get_cpf()[:3]}.{doador.get_cpf()[3:6]}.{doador.get_cpf()[6:9]}-{doador.get_cpf()[9:]}"
                opcoes.append(f"{doador.get_nome()} ({cpf}): {d.get_descricao()} - {d.get_tipo()} ({d.get_quantidade_doada()})")
                mapa.append(d)
            op = st.selectbox('Informe a doação', opcoes)
            submit = st.form_submit_button('Confirmar')
            if submit:
                try:
                    doacao = mapa[opcoes.index(op)]
                    DoacaoView.confirmar(doacao.get_id())
                    st.success('Doação confirmada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

class CPUI:
    def main():
        st.header('Confirmar Recebimento')
        i_f = st.session_state['id_usuario']
        produtos = [p for p in ProdutoView.listar() if p.get_id_favorecido() == i_f and p.get_situacao() == 'Em Entrega']
        if not produtos:
            st.write('Nenhum produto em rota de entrega')
            return
        with st.form('conf_produto'):
            opcoes, mapa = [], []
            for p in produtos:
                opcoes.append(f"{p.get_descricao()} - {p.get_tipo()} - {p.get_quantidade()}")
                mapa.append(p)
            op = st.selectbox('Informe o produto', opcoes)
            submit = st.form_submit_button('Confirmar')
            if submit:
                try:
                    produto = mapa[opcoes.index(op)]
                    ProdutoView.confirmar(produto.get_id())
                    st.success('Entrega confirmada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()