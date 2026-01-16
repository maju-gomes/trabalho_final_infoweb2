import streamlit as st
import pandas as pd
import time
from view import DoacaoView

class MDUI:
    def main():
        st.header('Doações')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Doar', 'Atualizar', 'Cancelar'])
        with tab1: MDUI.listar()
        with tab2: MDUI.doar()
        with tab3: MDUI.atualizar()
        with tab4: MDUI.cancelar()
    
    def listar():
        i_d = st.session_state['id_usuario']
        do = [d for d in DoacaoView.listar() if d.get_id_doador() == i_d]
        if not do:
            st.write('Nenhuma doação realizada')
        else:
            list_dic = []
            for obj in do:
                situacao = obj.get_situacao()
                if situacao == 'Pendente':
                    desc = f"{obj.get_descricao()} ({situacao})"
                else:
                    desc = obj.get_descricao()
                list_dic.append({
                    'Descrição':desc,
                    'Tipo':obj.get_tipo(),
                    'Quantidade':obj.get_quantidade_doada(),
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
        
    def doar():
        with st.form('ins_doacao'):
            desc = st.text_input('Informe a descrição', key='ins_doacao_desc')
            tipo = st.text_input('Informe o tipo', key='ins_doacao_tipo')
            qntd = st.text_input('Informe a quantidade', key='ins_doacao_qntd')
            submit = st.form_submit_button('Doar')
        if submit:
            try:
                id = st.session_state['id_usuario']
                DoacaoView.inserir(desc, tipo, qntd, 'Pendente', id)
                st.success('Doação registrada com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        i_d = st.session_state['id_usuario']
        doacoes = [d for d in DoacaoView.listar() if d.get_id_doador() == i_d and d.get_situacao() == 'Pendente']
        if not doacoes:
            st.write('Nenhuma doação pendente')
        else:
            with st.form('upd_doacao'):
                op = st.selectbox(
                    'Informe a doação',
                    doacoes,
                    format_func=lambda d:f"{d.get_descricao()} - {d.get_tipo()} ({d.get_quantidade_doada()})",
                    key='upd_doacao_op'
                )
                desc = st.text_input('Informe a descrição', op.get_descricao(), key='upd_doacao_desc')
                tipo = st.text_input('Informe o tipo', op.get_tipo(), key='upd_doacao_tipo')
                qntd = st.text_input('Informe a quantidade', str(op.get_quantidade_doada()), key='upd_doacao_qntd')
                submit = st.form_submit_button('Atualizar')
            if submit:
                try:
                    id = op.get_id()
                    DoacaoView.atualizar(id, desc, tipo, qntd, qntd, 'Pendente', i_d)
                    st.success('Doação atualizada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    
    def cancelar():
        i_d = st.session_state['id_usuario']
        doacoes = [d for d in DoacaoView.listar() if d.get_id_doador() == i_d and d.get_situacao() == 'Pendente']
        if not doacoes:
            st.write('Não há doações pendentes')
        else:
            with st.form('del_doacao'):
                op = st.selectbox(
                    'Informe a doação',
                    doacoes,
                    format_func=lambda d:f"{d.get_descricao()} - {d.get_tipo()} ({d.get_quantidade_doada()})",
                    key='del_doacao_op'
                )
                submit = st.form_submit_button('Cancelar')
            if submit:
                try:
                    DoacaoView.excluir(op.get_id())
                    st.success('Doação cancelada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()