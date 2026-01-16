import streamlit as st
import pandas as pd
import time
from view import DoacaoView, ProdutoView, FavorecidoView, EnderecoView

class RUI:
    def main():
        st.header('Reciclar')
        tab1, tab2, tab3, tab4 = st.tabs(['Solicitações', 'Estoque', 'Reciclar', 'Enviar'])
        with tab1: RUI.solicitacoes()
        with tab2: RUI.estoque()
        with tab3: RUI.reciclar()
        with tab4: RUI.enviar()

    def solicitacoes():
        produtos = [p for p in ProdutoView.listar() if p.get_situacao() != 'Entregue']
        list_dic = []
        if not produtos:
            st.write('Nenhum produto solicitado')
        else:
            for obj in produtos:
                fav = FavorecidoView.listar_id(obj.get_id_favorecido())
                cpf = f"{obj.get_cpf()[:3]}.{obj.get_cpf()[3:6]}.{obj.get_cpf()[6:9]}-{obj.get_cpf()[9:]}"
                list_dic.append({
                    'ID': obj.get_id(),
                    'Solicitante': f'{fav.get_nome()} ({cpf})',
                    'Descrição': obj.get_descricao(),
                    'Tipo': obj.get_tipo(),
                    'Quantidade': obj.get_quantidade(),
                    'Situação': obj.get_situacao()
                })
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def estoque():
        with st.expander('Doações'):
            doacoes = [d for d in DoacaoView.listar() if d.get_situacao() == 'Em Estoque']
            if not doacoes:
                st.write('Nenhuma doação em estoque')
            else:
                d = {}
                list_dic_do = []
                for obj in doacoes:
                    chave = (obj.get_descricao(), obj.get_tipo())
                    d[chave] = d.get(chave, 0) + obj.get_quantidade_disponivel()
                for (desc, tipo), qntd in d.items():
                    list_dic_do.append({
                        'Descrição':desc,
                        'Tipo':tipo,
                        'Quantidade':qntd
                    })
                df = pd.DataFrame(list_dic_do)
                st.dataframe(df)
        with st.expander('Produtos'):
            produtos = [p for p in ProdutoView.listar() if p.get_situacao() == 'Em Estoque']
            if not produtos:
                st.write('Nenhum produto em estoque')
            else:
                p = {}
                list_dic_pr = []
                for obj in produtos:
                    chave = (obj.get_descricao(), obj.get_tipo())
                    p[chave] = p.get(chave, 0) + obj.get_quantidade()
                for (desc, tipo), qntd in p.items():
                    list_dic_pr.append({
                        'Descrição':desc,
                        'Tipo':tipo,
                        'Quantidade':qntd
                    })
                df = pd.DataFrame(list_dic_pr)
                st.dataframe(df)

    def reciclar():
        doacoes = [d for d in DoacaoView.listar() if d.get_situacao() == 'Em Estoque']
        if not doacoes:
            st.write('Nenhuma doação em estoque')
            return
        with st.form('ins_produto'):
            opcoes_do = [f"{d.get_descricao()} - {d.get_tipo()} ({d.get_quantidade_disponivel()})" for d in doacoes]
            op_do = st.selectbox('Informe a doação', opcoes_do)
            doacao = doacoes[opcoes_do.index(op_do)]
            desc_do = doacao.get_descricao()
            qntd_di = doacao.get_quantidade_disponivel()
            qntd_usar = st.number_input('Informe a quantidade a ser utilizada', min_value=1, max_value=qntd_di, step=1)
            modo = st.radio('Modo', ['Atender Solicitação', 'Novo Produto'])
            if modo == 'Atender Solicitação':
                produtos = [p for p in ProdutoView.listar() if p.get_situacao() == 'Solicitado']
                if not produtos:
                    st.write('Nenhuma solicitação pendente')
                else:
                    opcoes_pr = [f"{p.get_id_favorecido()} - {p.get_descricao()} ({p.get_quantidade()})" for p in produtos]
                    op_pr = st.selectbox('Escolha a solicitação', opcoes_pr)
                    produto = produtos[opcoes_pr.index(op_pr)]
                    id_sol = produto.get_id()
                    desc_pr = produto.get_descricao()
                    tipo_pr = produto.get_tipo()
                    qntd_pr = produto.get_quantidade()
                    st.text_input('Produto', f'{desc_pr} - {tipo_pr}', disabled=True)
                    st.text_input('Quantidade', str(qntd_pr), disabled=True)
            else:
                desc_pr = st.text_input('Informe a descrição', key='ins_produto_desc')
                tipo_pr = st.text_input('Informe o tipo', key='ins_produto_tipo')
                qntd_pr = st.number_input('Informe a quantidade', min_value=1, step=1)
                id_sol = None
            submit = st.form_submit_button('Reciclar')
            if submit:
                try:
                    if modo == 'Atender Solicitação':
                        ProdutoView.atender_solicitacao(id_sol)
                    else:
                        ProdutoView.inserir(desc_do, qntd_usar, desc_pr, tipo_pr, qntd_pr, 'Em Estoque', None)
                    st.success('Doação reciclada com sucesso')
                except ValueError as erro:
                    st.error(erro)


    def enviar():
        sols = [p for p in ProdutoView.listar() if p.get_id_favorecido() != None]
        if not sols:
            st.write('Nenhuma solicitação em aberto')
            return
        with st.form('enviar_produto'):
            opcoes, ends = [], []
            for s in sols:
                fav = FavorecidoView.listar_id(s.get_id_favorecido())
                cpf = f"{fav.get_cpf()[:3]}.{fav.get_cpf()[3:6]}.{fav.get_cpf()[6:9]}-{fav.get_cpf()[9:]}"
                ends.append(EnderecoView.listar_id(fav.get_id_endereco()))
                nome = f"{fav.get_nome()} ({cpf})"
                opcoes.append(f'{nome} - {s.get_descricao()} - {s.get_tipo()} ({s.get_quantidade()})')
            op = st.selectbox('Informe a solicitação', opcoes)
            index = opcoes.index(op)
            pro = sols[index]
            end = ends[index]
            st.text_input('Produto', f'{pro.get_descricao()} - {pro.get_tipo()}', disabled=True)
            st.text_input('Quantidade', str(pro.get_quantidade()), disabled=True)
            e = f"{end.get_rua()}, {end.get_numero()} - {end.get_bairro()}, {end.get_cidade()}/{end.get_uf()} | CEP: {end.get_cep()}"
            if end.get_complemento():
                e += f" | {end.get_complemento()}"
            st.text_input('Endereço', e, disabled=True)
            submit = st.form_submit_button('Enviar')
            if submit:
                try:
                    if pro.get_situacao() == 'Em Estoque':
                        ProdutoView.atualizar(
                            pro.get_id(),
                            pro.get_descricao(),
                            pro.get_tipo(),
                            pro.get_quantidade(),
                            'Em Entrega',
                            pro.get_id_favorecido()
                        )
                    else:
                        ProdutoView.atender_solicitacao(pro.get_id())
                    st.success('Produto enviado com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()