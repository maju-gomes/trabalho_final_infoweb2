import streamlit as st
import pandas as pd
import time
from view.view import DoacaoView, ProdutoView, FavorecidoView, EnderecoView

class RUI:
    def main():
        st.header('Reciclar')
        tab1, tab2, tab3, tab4 = st.tabs(['Solicitações', 'Estoque', 'Reciclar', 'Enviar'])
        with tab1: RUI.solicitacoes()
        with tab2: RUI.estoque()
        with tab3: RUI.reciclar()
        with tab4: RUI.enviar()

    def solicitacoes():
        produtos = [p for p in ProdutoView.listar() if not (p.get_situacao() == 'Em Estoque' and p.get_id_favorecido() is None)]
        list_dic = []
        if not produtos:
            st.write('Nenhum produto solicitado')
        else:
            for obj in produtos:
                fav = FavorecidoView.listar_id(obj.get_id_favorecido())
                cpf = f"{fav.get_cpf()[:3]}.{fav.get_cpf()[3:6]}.{fav.get_cpf()[6:9]}-{fav.get_cpf()[9:]}"
                list_dic.append({
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
        if not 'modo_reciclar' in st.session_state:
            st.session_state.modo_reciclar = 'Atender Solicitação'
        st.radio('Modo', ['Atender Solicitação', 'Novo Produto'], key='modo_reciclar')
        with st.form('ins_produto'):
            opcoes_do = []
            i = {}
            for d in doacoes:
                chave = (d.get_descricao(), d.get_tipo())
                i[chave] = i.get(chave, 0) + d.get_quantidade_disponivel()
            for (desc, tipo), qntd in i.items():
                opcoes_do.append({
                    'd':desc,
                    't':tipo,
                    'q':qntd
                })            
            op_do = st.selectbox('Informe a doação', opcoes_do, format_func=lambda x:f"{x['d']} - {x['t']} ({x['q']})")
            qntd_di = op_do['q']
            desc_do = op_do['d']          
            qntd_usar = st.number_input('Informe a quantidade a ser utilizada', min_value=1, max_value=qntd_di, step=1)
            if st.session_state.modo_reciclar == 'Atender Solicitação':
                produtos = [p for p in ProdutoView.listar() if p.get_situacao() == 'Solicitado']
                if not produtos:
                    st.write('Nenhuma solicitação pendente')
                    dis = True
                else:
                    dis = False
                    opcoes_pr = []
                    for p in produtos:
                        fav = FavorecidoView.listar_id(p.get_id_favorecido())
                        cpf = f"{fav.get_cpf()[:3]}.{fav.get_cpf()[3:6]}.{fav.get_cpf()[6:9]}-{fav.get_cpf()[9:]}"
                        opcoes_pr.append(f"{fav.get_nome()} ({cpf}) - {p.get_descricao()} ({p.get_quantidade()})")
                    op_pr = st.selectbox('Escolha a solicitação', opcoes_pr)
                    produto = produtos[opcoes_pr.index(op_pr)]
                    id_sol = produto.get_id()
                    desc_pr = produto.get_descricao()
                    tipo_pr = produto.get_tipo()
                    qntd_pr = produto.get_quantidade()
                    st.text_input('Produto', f'{desc_pr} - {tipo_pr}', disabled=True)
                    st.text_input('Quantidade', str(qntd_pr), disabled=True)
            else:
                dis = False
                desc_pr = st.text_input('Informe a descrição', key='ins_produto_desc')
                tipo_pr = st.text_input('Informe o tipo', key='ins_produto_tipo')
                qntd_pr = st.number_input('Informe a quantidade', min_value=1, step=1)
            submit = st.form_submit_button('Reciclar', disabled=dis)
            if submit:
                try:
                    if st.session_state.modo_reciclar == 'Atender Solicitação':
                        ProdutoView.atender_solicitacao(id_sol, 'Em Estoque', desc_do, qntd_usar)
                    else:
                        ProdutoView.inserir(desc_pr, tipo_pr, qntd_pr, 'Em Estoque', None, desc_do, qntd_usar)
                    st.success('Doação reciclada com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def enviar():
        sols = [p for p in ProdutoView.listar() if p.get_situacao() in ['Solicitado', 'Em Estoque'] and p.get_id_favorecido() is not None]
        if not sols:
            st.write('Nenhuma solicitação pendente')
            return
        with st.form('enviar_produto'):
            opcoes_sol, ends = [], []
            for s in sols:
                fav = FavorecidoView.listar_id(s.get_id_favorecido())
                cpf = f"{fav.get_cpf()[:3]}.{fav.get_cpf()[3:6]}.{fav.get_cpf()[6:9]}-{fav.get_cpf()[9:]}"
                ends.append(EnderecoView.listar_id(fav.get_id_endereco()))
                nome = f"{fav.get_nome()} ({cpf})"
                opcoes_sol.append(f'{nome} - {s.get_descricao()} - {s.get_tipo()} ({s.get_quantidade()})')
            op_sol = st.selectbox('Informe a solicitação', opcoes_sol)
            index = opcoes_sol.index(op_sol)
            pro = sols[index]
            id_sol = pro.get_id()
            end = ends[index]
            cep = f"{end.get_cep()[:5]}-{end.get_cep()[5:]}"
            e = f"{end.get_rua()}, {end.get_numero()} - {end.get_bairro()}, {end.get_cidade()}/{end.get_uf()} | CEP: {cep}"
            if end.get_complemento():
                e += f" | {end.get_complemento()}"
            st.text_input('Endereço', e, disabled=True)
            if pro.get_situacao() == 'Em Estoque':
                st.text_input('Produto', f"{pro.get_descricao()} - {pro.get_tipo()}" , disabled=True)
                st.number_input('Quantidade', pro.get_quantidade(), disabled=True)
                dis = False
            else:
                produtos = [p for p in ProdutoView.listar() if p.get_situacao() == 'Em Estoque' and p.get_id_favorecido() is None and p.get_descricao() == pro.get_descricao() and p.get_tipo() == pro.get_tipo()]
                if not produtos:
                    st.write('Produto indisponível em estoque')
                    dis = True
                else:
                    dis = False
                    opcoes_pro = []
                    qntd_total = sum(p.get_quantidade() for p in produtos)
                    opcoes_pro.append({
                        'd':pro.get_descricao(),
                        't':pro.get_tipo(),
                        'q':qntd_total
                    })
                    op_pro = opcoes_pro[0]
                    if op_pro['q'] < pro.get_quantidade():
                        st.write('Estoque insuficiente')
                        dis = True
                    else:
                        op_pro = st.selectbox('Produto', opcoes_pro, format_func=lambda x:f"{x['d']} - {x['t']} ({x['q']})", disabled=True)
                        qntd_pro = st.number_input('Quantidade', pro.get_quantidade(), disabled=True)
                        desc_pro = pro.get_descricao()
            submit = st.form_submit_button('Enviar', disabled=dis)
            if submit:
                try:
                    if pro.get_situacao() == 'Em Estoque':
                        ProdutoView.atualizar(
                            id_sol,
                            pro.get_descricao(),
                            pro.get_tipo(),
                            pro.get_quantidade(),
                            'Em Entrega',
                            pro.get_id_favorecido()
                        )
                    else:
                        ProdutoView.atender_solicitacao(id_sol, 'Em Entrega', desc_pro, qntd_pro)
                    st.success('Produto enviado com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()