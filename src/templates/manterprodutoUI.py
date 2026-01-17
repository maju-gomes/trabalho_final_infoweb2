import streamlit as st
import pandas as pd
import time
from view import ProdutoView

class MPUI:
    def main():
        st.header('Produtos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Solicitar', 'Atualizar', 'Cancelar'])
        with tab1: MPUI.listar()
        with tab2: MPUI.solicitar()
        with tab3: MPUI.atualizar()
        with tab4: MPUI.cancelar()

    def listar():
        i_f = st.session_state['id_usuario']
        produtos = [p for p in ProdutoView.listar() if p.get_id_favorecido() == i_f]
        if not produtos:
            st.write('Nenhum produto vinculado')
        else:
            list_dic = []
            for obj in produtos:
                list_dic.append({
                    'Descrição':obj.get_descricao(),
                    'Tipo':obj.get_tipo(),
                    'Quantidade':obj.get_quantidade(),
                    'Situação':obj.get_situacao()
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def solicitar():
        with st.form('sol_produto'):
            desc = st.text_input('Informe a descrição', key='sol_produto_desc')
            tipo = st.text_input('Informe o tipo', key='sol_produto_tipo')
            qntd = st.number_input('Informe a quantidade', key='sol_produto_qntd', min_value=0, step=1)
            submit = st.form_submit_button('Solicitar')
            if submit:
                try:
                    id = st.session_state['id_usuario']
                    ProdutoView.inserir(desc, tipo, qntd, 'Solicitado', id)
                    st.success('Produto solicitado com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    
    def atualizar():
        i_f = st.session_state['id_usuario']
        produtos = [p for p in ProdutoView.listar() if p.get_id_favorecido() == i_f and p.get_situacao() != 'Entregue']
        if not produtos:
            st.write('Nenhum produto solicitado')
        else:
            with st.form('upd_sol_produto'):
                op = st.selectbox(
                    'Informe o produto',
                    produtos,
                    format_func=lambda p:f"{p.get_descricao()} - {p.get_tipo()} ({p.get_quantidade()})",
                    key='upd_sol_produto_op'
                )
                desc = st.text_input('Informe a descrição', op.get_descricao(), key='upd_sol_produto_desc')
                tipo = st.text_input('Informe o tipo', op.get_tipo(), key='upd_sol_produto_tipo')
                qntd = st.number_input('Informe a quantidade', value=op.get_quantidade(), key='upd_sol_produto_qntd', min_value=0, step=1)
                submit = st.form_submit_button('Atualizar')
                if submit:
                    try:
                        id = op.get_id()
                        ProdutoView.atualizar_solicitacao(id, desc, tipo, op.get_quantidade(), qntd, op.get_situacao(), i_f)
                        st.success('Solicitação atualizada com sucesso')
                    except ValueError as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()
    
    def cancelar():
        i_f = st.session_state['id_usuario']
        produtos = [p for p in ProdutoView.listar() if p.get_id_favorecido() == i_f and p.get_situacao() != 'Entregue']
        if not produtos:
            st.write('Nenhum produto solicitado')
        else:
            with st.form('del_sol_produto'):
                op = st.selectbox(
                    'Informe o produto',
                    produtos,
                    format_func=lambda p:f"{p.get_descricao()} - {p.get_tipo()} ({p.get_quantidade()})",
                    key='del_sol_produto_op'
                )
                submit = st.form_submit_button('Cancelar')
                if submit:
                    try:
                        ProdutoView.excluir(op.get_id(), op.get_situacao())
                        st.success('Solicitação cancelada com sucesso')
                    except ValueError as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()