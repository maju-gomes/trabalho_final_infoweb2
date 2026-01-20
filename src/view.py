from model.usuarios import Admin, Doador, Favorecido, Usuario
from model.endereco import Endereco
from model.doacao_produto import Doacao, Produto
from dao.usuariosDAO import AdminDAO, DoadorDAO, FavorecidoDAO, UsuarioDAO
from dao.enderecoDAO import EnderecoDAO
from dao.doacao_produtoDAO import DoacaoDAO, ProdutoDAO

class UsuarioView:
    @staticmethod
    def listar():
        u = UsuarioDAO.listar()
        u.sort(key=lambda obj: obj.get_nome())
        return u
    
    @staticmethod
    def excluir(id):
        UsuarioDAO.excluir(id)

class AdminView:
    @staticmethod
    def inserir(nome, email, senha, cnpj):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cnpjs = [obj.get_cnpj() for obj in AdminView.listar()]
        cnpj_for = ''.join(c for c in cnpj if c.isdigit())
        if email.strip().lower() in emails:
            raise ValueError('E-mail já cadastrado')
        if cnpj_for in cnpjs:
            raise ValueError('CNPJ já cadastrado')
        a = Admin(None, nome, email, senha, cnpj)
        AdminDAO.inserir(a)

    @staticmethod
    def listar():
        a = AdminDAO.listar()
        a.sort(key=lambda obj: obj.get_nome())
        return a
    
    @staticmethod
    def listar_id(id):
        return AdminDAO.listar_id(id)

    @staticmethod
    def atualizar(id, nome, email, senha, cnpj):
        atual = AdminView.listar_id(id)
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cnpjs = [obj.get_cnpj() for obj in AdminView.listar()]
        cnpj_for = ''.join(c for c in cnpj if c.isdigit())
        email_for = email.strip().lower()
        if email_for != atual.get_email():
            if email_for in emails:
                raise ValueError('E-mail já cadastrado')
        if cnpj_for != atual.get_cnpj():
            if cnpj_for in cnpjs:
                raise ValueError('CNPJ já cadastrado')
        a = Admin(id, nome, email, senha, cnpj)
        AdminDAO.atualizar(a)

    @staticmethod
    def excluir(id):
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email_cnpj, senha):
        email_cnpj = email_cnpj.strip()
        cnpj = ''.join(c for c in email_cnpj if c.isdigit())
        if cnpj:
            for obj in AdminView.listar():
                if cnpj == obj.get_cnpj() and obj.get_senha() == senha:
                    return obj
        email = email_cnpj.lower()
        for obj in AdminView.listar():
            if email == obj.get_email() and obj.get_senha() == senha:
                return obj
        return None


class DoadorView:
    @staticmethod
    def inserir(nome, email, senha, cpf, tel):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()] + [obj.get_telefone() for obj in FavorecidoView.listar()]
        email_for = email.strip().lower()
        cpf_for = ''.join(c for c in cpf if c.isdigit())
        tel_for = ''.join(c for c in tel if c.isdigit())
        if email_for in emails:
            raise ValueError('E-mail já cadastrado')
        if cpf_for in cpfs:
            raise ValueError('CPF já cadastrado')
        if tel_for in tels:
            raise ValueError('Telefone já cadastrado')
        d = Doador(None, nome, email, senha, cpf, tel)
        DoadorDAO.inserir(d)

    @staticmethod
    def listar():
        d = DoadorDAO.listar()
        d.sort(key=lambda obj:obj.get_nome())
        return d
    
    @staticmethod
    def listar_id(id):
        return DoadorDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, nome, email, senha, cpf, tel):
        atual = DoadorView.listar_id(id)
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()] + [obj.get_telefone() for obj in FavorecidoView.listar()]
        email_for = ''.join(c for c in email if c.isdigit())
        cpf_for = ''.join(c for c in cpf if c.isdigit())
        tel_for = ''.join(c for c in tel if c.isdigit())
        if email_for != atual.get_email():
            if email_for in emails:
                raise ValueError('E-mail já cadastrado')
        if cpf_for != atual.get_cpf():
            if cpf_for in cpfs:
                raise ValueError('CPF já cadastrado')
        if tel_for != atual.get_telefone():
            if tel_for in tels:
                raise ValueError('Telefone já cadastrado')
        d = Doador(id, nome, email, senha, cpf, tel)
        DoadorDAO.atualizar(d)

    @staticmethod
    def excluir(id):
        do = [d for d in DoacaoView.listar() if d.get_id_doador() == id]
        if do:
            for obj in do:
                if obj.get_situacao() == 'Usada':
                    DoacaoView.excluir(obj.get_id())
                elif obj.get_situacao() == 'Em Estoque':
                    DoacaoView.atualizar(
                        obj.get_id(),
                        obj.get_descricao(),
                        obj.get_tipo(),
                        obj.get_quantidade_doada(),
                        obj.get_quantidade_disponivel(),
                        obj.get_situacao(),
                        None
                        )
                else:
                    raise ValueError('Há doações em aberto')
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email_cpf, senha):
        email_cpf = email_cpf.strip()
        cpf = ''.join(c for c in email_cpf if c.isdigit())
        if cpf:
            for obj in DoadorView.listar():
                if cpf == obj.get_cpf() and obj.get_senha() == senha:
                    return obj
        email = email_cpf.lower()
        for obj in DoadorView.listar():
            if email == obj.get_email() and obj.get_senha() == senha:
                return obj
        return None


class FavorecidoView:
    @staticmethod
    def inserir(nome, email, senha, cpf, tel, i_e):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()]
        email_for = ''.join(c for c in email if c.isdigit())
        cpf_for = ''.join(c for c in cpf if c.isdigit())
        tel_for = ''.join(c for c in tel if c.isdigit())
        if email_for in emails:
            raise ValueError('E-mail já cadastrado')
        if cpf_for in cpfs:
            raise ValueError('CPF já cadastrado')
        if tel_for in tels:
            raise ValueError('Telefone já cadastrado')
        f = Favorecido(None, nome, email, senha, cpf, tel, i_e)
        FavorecidoDAO.inserir(f)

    @staticmethod
    def listar():
        f = FavorecidoDAO.listar()
        f.sort(key=lambda obj: obj.get_nome())
        return f
    
    @staticmethod
    def listar_id(id):
        return FavorecidoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, nome, email, senha, cpf, tel, i_e):
        atual = FavorecidoDAO.listar_id(id)
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()]
        email_for = ''.join(c for c in email if c.isdigit())
        cpf_for = ''.join(c for c in cpf if c.isdigit())
        tel_for = ''.join(c for c in tel if c.isdigit())        
        if email_for != atual.get_email():
            if email_for in emails:
                raise ValueError('E-mail já cadastrado')
        if cpf_for != atual.get_cpf():
            if cpf_for in cpfs:
                raise ValueError('CPF já cadastrado')
        if tel_for != atual.get_telefone():
            if tel_for in tels:
                raise ValueError('Telefone já cadastrado')
        f = Favorecido(id, nome, email, senha, cpf, tel, i_e)
        FavorecidoDAO.atualizar(f)

    @staticmethod
    def excluir(id):
        pro =  [p for p in ProdutoView.listar() if p.get_id_favorecido() == id]
        if pro:
            for obj in pro:
                if obj.get_situacao() in ['Solicitado', 'Entregue']:
                    ProdutoView.excluir(obj.get_id())
                elif obj.get_situacao() == 'Em Estoque':
                    ProdutoView.atualizar(obj.get_id(), obj.get_descricao(), obj.get_tipo(), obj.get_quantidade(), None)
                else:
                    raise ValueError('Há produtos em rota de entrega pra este usuário')
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email_cpf, senha):
        email_cpf = email_cpf.strip()
        cpf = ''.join(c for c in email_cpf if c.isdigit())
        if cpf:
            for obj in FavorecidoView.listar():
                if cpf == obj.get_cpf() and obj.get_senha() == senha:
                    return obj
        email = email_cpf.lower()
        for obj in FavorecidoView.listar():
            if email == obj.get_email() and obj.get_senha() == senha:
                return obj
        return None
    
class EnderecoView:
    @staticmethod
    def inserir(cep, uf, ci, b, r, num, com):
        id = None
        ends = EnderecoView.listar()
        for end in ends:
            if (
                end.get_cep() == cep and
                end.get_uf() == uf and
                end.get_cidade() == ci and
                end.get_bairro() == b and
                end.get_rua() == r and
                end.get_numero() == num and
                (end.get_complemento() or '') == (com or '')
            ):
                id = end.get_id()
                break
        if id is None:
            e = Endereco(None, cep, uf, ci, b, r, num, com)
            id = EnderecoDAO.inserir(e)
        return id
    
    @staticmethod
    def listar():
        e = EnderecoDAO.listar()
        e.sort(key=lambda obj: (obj.get_uf(), obj.get_cidade(), obj.get_bairro(), obj.get_rua(), obj.get_numero()))
        return e
        
    @staticmethod
    def listar_id(id):
        return EnderecoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(cep, uf, ci, b, r, num, com):
        id = EnderecoView.inserir(cep, uf, ci, b, r, num, com)
        return id
    
    @staticmethod
    def excluir(id):
        ends = [obj.get_id_endereco() for obj in FavorecidoView.listar()]
        if id not in ends:
            EnderecoDAO.excluir(id)

class DoacaoView:
    @staticmethod
    def inserir(descricao, tipo, qntd, situacao, id_doador):
        d = Doacao(None, descricao, tipo, qntd, qntd, situacao, id_doador)
        DoacaoDAO.inserir(d)

    @staticmethod
    def listar():
        d = DoacaoDAO.listar()
        d.sort(key=lambda obj:obj.get_descricao())
        return d
    
    @staticmethod
    def listar_id(id):
        return DoacaoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, descricao, tipo, qntd_do, qntd_di, situacao, id_doador):
        d = Doacao(id, descricao, tipo, qntd_do, qntd_di, situacao, id_doador)
        DoacaoDAO.atualizar(d)

    @staticmethod
    def confirmar(id):
        d = DoacaoView.listar_id(id)
        DoacaoView.atualizar(id, d.get_descricao(), d.get_tipo(), d.get_quantidade_doada(), d.get_quantidade_disponivel(), 'Em Estoque', d.get_id_doador())

    @staticmethod
    def excluir(id, situacao=None):
        if situacao != 'Pendente':
            raise ValueError('Doação já entregue')
        DoacaoDAO.excluir(id)

class ProdutoView:
    @staticmethod
    def inserir(descricao, tipo, qntd_produto, situacao, id_favorecido, descricao_doacao=None, qntd_doacao=None):
        p = Produto(None, descricao, tipo, qntd_produto, situacao, id_favorecido)
        ProdutoDAO.inserir(p)
        if descricao_doacao is not None and qntd_doacao is not None:
            doacoes: list[Doacao] = []
            disp = 0
            usado = 0
            for d in DoacaoView.listar():
                if d.get_situacao() == 'Em Estoque' and d.get_descricao() == descricao_doacao:
                    doacoes.append(d)
                    disp += d.get_quantidade_disponivel()
            if disp < qntd_doacao:
                raise ValueError('Quantidade de Doações Indisponível')
            for d in doacoes:
                if usado >= qntd_doacao:
                    break
                disponivel = d.get_quantidade_disponivel()
                falta = qntd_doacao - usado
                if disponivel <= falta:
                    usado += disponivel
                    nova_disp = 0
                    situacao_doacao = 'Usada'
                else:
                    usado += falta
                    nova_disp = disponivel - falta
                    situacao_doacao = 'Em Estoque'
                DoacaoView.atualizar(
                    d.get_id(),
                    d.get_descricao(),
                    d.get_tipo(),
                    d.get_quantidade_doada(),
                    nova_disp,
                    situacao_doacao,
                    d.get_id_doador()
                )

    @staticmethod
    def listar():
        p = ProdutoDAO.listar()
        p.sort(key=lambda obj:obj.get_descricao())
        return p
    
    @staticmethod
    def listar_id(id):
        return ProdutoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id_produto, descricao, tipo, qntd_produto, situacao_produto, id_favorecido, descricao_doacao=None, qntd_doacao=None):
        if descricao_doacao is not None and qntd_doacao is not None:
            doacoes: list[Doacao] = []
            disp = 0
            usado = 0
            for d in DoacaoView.listar():
                if d.get_situacao() == 'Em Estoque' and d.get_descricao() == descricao_doacao:
                    doacoes.append(d)
                    disp += d.get_quantidade_disponivel()
            if disp < qntd_doacao:
                raise ValueError('Quantidade de Doações Indisponível')
            for d in doacoes:
                if usado >= qntd_doacao:
                    break
                disponivel = d.get_quantidade_disponivel()
                falta = qntd_doacao - usado
                if disponivel <= falta:
                    usado += disponivel
                    nova_disp = 0
                    situacao_doacao = 'Usada'
                else:
                    usado += falta
                    nova_disp = disponivel - falta
                    situacao_doacao = 'Em Estoque'
                DoacaoView.atualizar(
                    d.get_id(),
                    d.get_descricao(),
                    d.get_tipo(),
                    d.get_quantidade_doada(),
                    nova_disp,
                    situacao_doacao,
                    d.get_id_doador()
                )
        p = Produto(id_produto, descricao, tipo, qntd_produto, situacao_produto, id_favorecido)
        ProdutoDAO.atualizar(p)

    @staticmethod
    def atualizar_solicitacao(id_produto, descricao, tipo, qntd_primaria, qntd_nova, situacao, id_favorecido):
        if situacao == 'Em Estoque' and qntd_primaria != qntd_nova:
            raise ValueError('Solicitação já atendida. Não é possível mudar a quantidade')
        if situacao == 'Em Entrega':
            raise ValueError('Produto em rota de entrega')
        ProdutoView.atualizar(id_produto, descricao, tipo, qntd_nova, situacao, id_favorecido)

    @staticmethod
    def atender_solicitacao(id_solicitacao, situacao, descricao, qntd):
        if situacao == 'Em Estoque':
            doacoes = []
            disp = 0
            usado = 0
            for d in DoacaoView.listar():
                if d.get_situacao() == 'Em Estoque' and d.get_descricao() == descricao:
                    doacoes.append(d)
                    disp += d.get_quantidade_disponivel()
            if disp < qntd:
                raise ValueError('Quantidade de Doações Indisponível')
            for d in doacoes:
                if usado >= qntd:
                    break
                disponivel = d.get_quantidade_disponivel()
                falta = qntd - usado
                if disponivel <= falta:
                    usado += disponivel
                    nova_disp = 0
                    situacao_doacao = 'Usada'
                else:
                    usado += falta
                    nova_disp = disponivel - falta
                    situacao_doacao = 'Em Estoque'
                DoacaoView.atualizar(
                    d.get_id(),
                    d.get_descricao(),
                    d.get_tipo(),
                    d.get_quantidade_doada(),
                    nova_disp,
                    situacao_doacao,
                    d.get_id_doador()
                )
        elif situacao == 'Em Entrega':
            produtos = []
            disp = 0
            usado = 0
            id_prod_entrega = None
            sol = ProdutoView.listar_id(id_solicitacao)
            id_fav = sol.get_id_favorecido()

            for p in ProdutoView.listar():
                if (p.get_situacao() == 'Em Estoque'
                    and p.get_id_favorecido() is None
                    and p.get_descricao() == descricao):
                    produtos.append(p)
                    disp += p.get_quantidade()
            if disp < qntd:
                raise ValueError('Estoque de produtos insuficiente')
            for p in produtos:
                if usado >= qntd:
                    break
                disponivel = p.get_quantidade()
                falta = qntd - usado
                if disponivel <= falta:
                    usado += disponivel
                    if id_prod_entrega is None:
                        ProdutoView.atualizar(
                            p.get_id(),
                            p.get_descricao(),
                            p.get_tipo(),
                            disponivel,
                            'Em Entrega',
                            id_fav
                        )
                        id_prod_entrega = p.get_id()
                    else:
                        prod_entrega = ProdutoView.listar_id(id_prod_entrega)
                        ProdutoView.atualizar(
                            prod_entrega.get_id(),
                            prod_entrega.get_descricao(),
                            prod_entrega.get_tipo(),
                            prod_entrega.get_quantidade() + disponivel,
                            'Em Entrega',
                            id_fav
                        )
                        ProdutoView.excluir(p.get_id())
                else:
                    usado += falta
                    sobra = disponivel - falta
                    if id_prod_entrega is None:
                        ProdutoView.atualizar(
                            p.get_id(),
                            p.get_descricao(),
                            p.get_tipo(),
                            falta,
                            'Em Entrega',
                            id_fav
                        )
                        id_prod_entrega = p.get_id()
                        ProdutoView.inserir(
                            p.get_descricao(),
                            p.get_tipo(),
                            sobra,
                            'Em Estoque',
                            None
                        )
                    else:
                        prod_entrega = ProdutoView.listar_id(id_prod_entrega)
                        ProdutoView.atualizar(
                            prod_entrega.get_id(),
                            prod_entrega.get_descricao(),
                            prod_entrega.get_tipo(),
                            prod_entrega.get_quantidade() + falta,
                            'Em Entrega',
                            id_fav
                        )
                        ProdutoView.atualizar(
                            p.get_id(),
                            p.get_descricao(),
                            p.get_tipo(),
                            sobra,
                            'Em Estoque',
                            None
                        )
        ProdutoView.excluir(id_solicitacao)

    @staticmethod
    def confirmar(id):
        p = ProdutoView.listar_id(id)
        ProdutoView.atualizar(id, p.get_descricao(), p.get_tipo(), p.get_quantidade(), 'Entregue', p.get_id_favorecido())

    @staticmethod
    def excluir(id, situacao=None):
        if situacao == 'Em Estoque':
            raise ValueError('Solicitação já atendida')
        if situacao == 'Em Entrega':
            raise ValueError('Produto em rota de entrega')
        ProdutoDAO.excluir(id)