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
        u = Usuario(id, 'None', 'None@', 'None')
        UsuarioDAO.excluir(u)

class AdminView:
    @staticmethod
    def inserir(nome, email, senha, cnpj):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cnpjs = [obj.get_cnpj() for obj in AdminView.listar()]
        if email in emails:
            raise ValueError('E-mail já cadastrado')
        if cnpj in cnpjs:
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
        if email != atual.get_email():
            if email in emails:
                raise ValueError('E-mail já cadastrado')
        if cnpj != atual.get_cnpj():
            if cnpj in cnpjs:
                raise ValueError('CNPJ já cadastrado')
        a = Admin(id, nome, email, senha, cnpj)
        AdminDAO.atualizar(a)

    @staticmethod
    def excluir(id):
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email, senha):
        for obj in AdminView.listar():
            if obj.get_email() == email and obj.get_senha() == senha:
                return obj
        return None


class DoadorView:
    @staticmethod
    def inserir(nome, email, senha, cpf, tel):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()] + [obj.get_telefone() for obj in FavorecidoView.listar()]
        if email in emails:
            raise ValueError('E-mail já cadastrado')
        if cpf in cpfs:
            raise ValueError('CPF já cadastrado')
        if tel in tels:
            raise ValueError('Telefone já cadastrado')
        d = Doador(None, nome, email, senha, cpf, tel)
        DoadorDAO.inserir(d)

    @staticmethod
    def listar():
        d = DoadorDAO.listar()

        d.sort(key=lambda d:d.nome)

        lista_d = []
        for doador in d:
            lista_d.append({
                "id": doador.doador,
                "nome": doador.nome,
                "email": doador.email,
                "cpf": doador.cpf,
                "telefone": doador.telefone
            })

        return lista_d
    
    @staticmethod
    def listar_id(id):
        return DoadorDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, nome, email, senha, cpf, tel):
        atual = DoadorView.listar_id(id)
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()] + [obj.get_telefone() for obj in FavorecidoView.listar()]
        if email != atual.get_email():
            if email in emails:
                raise ValueError('E-mail já cadastrado')
        if cpf != atual.get_cpf():
            if cpf in cpfs:
                raise ValueError('CPF já cadastrado')
        if tel != atual.get_telefone():
            if tel in tels:
                raise ValueError('Telefone já cadastrado')
        d = Doador(id, nome, email, senha, cpf, tel)
        DoadorDAO.atualizar(d)

    @staticmethod
    def excluir(id):
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email, senha):
        for obj in DoadorView.listar():
            if obj.get_email() == email and obj.get_senha() == senha:
                return obj
        return None


class FavorecidoView:
    @staticmethod
    def inserir(nome, email, senha, cpf, tel, cep, uf, ci, b, r, n, co):
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()]
        if email in emails:
            raise ValueError('E-mail já cadastrado')
        if cpf in cpfs:
            raise ValueError('CPF já cadastrado')
        if tel in tels:
            raise ValueError('Telefone já cadastrado')
        i_e = EnderecoView.inserir(cep, uf, ci, b, r, n, co)
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
    def atualizar(id, nome, email, senha, cpf, tel, cep, uf, ci, b, r, n, co):
        atual = FavorecidoDAO.listar_id(id)
        emails = [obj.get_email() for obj in UsuarioView.listar()]
        cpfs = [obj.get_cpf() for obj in DoadorView.listar()] + [obj.get_cpf() for obj in FavorecidoView.listar()]
        tels = [obj.get_telefone() for obj in DoadorView.listar()]
        if email != atual.get_email():
            if email in emails:
                raise ValueError('E-mail já cadastrado')
        if cpf != atual.get_cpf():
            if cpf in cpfs:
                raise ValueError('CPF já cadastrado')
        if tel != atual.get_telefone():
            if tel in tels:
                raise ValueError('Telefone já cadastrado')
        i_e = EnderecoView.atualizar(cep, uf, ci, b, r, n, co)
        f = Favorecido(id, nome, email, senha, cpf, tel, i_e)
        FavorecidoDAO.atualizar(f)

    @staticmethod
    def excluir(id):
        UsuarioView.excluir(id)

    @staticmethod
    def autenticar(email, senha):
        for obj in FavorecidoView.listar():
            if obj.get_email() == email and obj.get_senha() == senha:
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
        if id == None:
            e = Endereco(None, cep, uf, ci, b, r, num, com)
            EnderecoDAO.inserir(e)
            id = e.get_id()
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
        if id in ends:
            raise ValueError('Endereço vinculado a um usuário')
        e = Endereco(id, '11111-111', 'NN', 'None', 'None', 'None', '11', None)
        EnderecoDAO.excluir(e)

class DoacaoView:
    @staticmethod
    def inserir(descricao, tipo, qntd, id_doador):
        d = Doacao(None, descricao, tipo, qntd, id_doador)
        DoacaoDAO.inserir(d)

    @staticmethod
    def listar():
        doacoes = DoacaoDAO.listar()
        doacoes.sort(key=lambda obj:obj.get_descricao())

    @staticmethod
    def listar_resumido():
        d = DoacaoDAO.listar()
        d.sort(key=lambda obj: obj.get_descricao())
        return d
    
    @staticmethod
    def listar_id(id):
        return DoacaoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, descricao, tipo, qntd, id_doador):
        d = Doacao(id, descricao, tipo, qntd, id_doador)
        DoacaoDAO.atualizar(d)

    @staticmethod
    def excluir(id):
        d = Doacao(id, 'None', 'None', 1, 'None')
        DoacaoDAO.excluir(d)

class ProdutoView:
    @staticmethod
    def inserir(descricao_doacao, qntd_doacao, descricao, tipo, qntd_produto, id_fav):
        doacoes = []
        qntds = 0
        for d in DoacaoDAO.listar():
            if d.get_situacao() == None and d.get_descricao() == descricao_doacao:
                doacoes.append({'id':d.get_id(), 'qntd':d.get_quantidade()})
        while qntds !=
        p = Produto(None, descricao, tipo, qntd_produto, id_fav)
        ProdutoDAO.inserir(p)

    @staticmethod
    def listar():
        p = ProdutoDAO.listar()
        p.sort(key=lambda obj:obj.get_descricao())
        return p
    
    @staticmethod
    def listar_id(id):
        return ProdutoDAO.listar_id(id)
    
    @staticmethod
    def atualizar(id, descricao, tipo, qntd, id_doador):
        d = Produto(id, descricao, tipo, qntd, id_doador)
        ProdutoDAO.atualizar(d)

    @staticmethod
    def excluir(id):
        d = Produto(id, 'None', 'None', 1, 'None')
        ProdutoDAO.excluir(d)