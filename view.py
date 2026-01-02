from model.usuarios import Usuario, Doador, Favorecido
from dao.usuariosDAO import UsuarioDAO, DoadorDAO, FavorecidoDAO

class UsuarioView:
    @staticmethod
    def listar_usuario():
        usuario = UsuarioDAO.listar()
        usuario.sort(key=lambda obj: obj.get_nome())
        return usuario
    
    @staticmethod
    def listar_id_usuario(id):
        return UsuarioDAO.listar_id(id)
    
    @staticmethod
    def inserir_usuario(nome, email, senha):
        usuario = Usuario(0, nome, email, senha)
        UsuarioDAO.inserir(usuario)

    @staticmethod
    def atualizar_usuario(id, nome, email, senha):
        usuario = Usuario(id, nome, email, senha)
        UsuarioDAO.atualizar(usuario)

    @staticmethod
    def excluir_usuario(id):
        usuario = Usuario(id, "", "", "")
        UsuarioDAO.excluir(usuario)

    @staticmethod
    def criar_usuario_admin():
        for usuario in UsuarioView.listar_usuario():
            if usuario.get_email() == "admin": return
        UsuarioView.inserir_usuario("admin", "admin", "1234")


class FavorecidoView:
    @staticmethod
    def listar_favorecido():
        favorecido = FavorecidoDAO.listar()
        favorecido.sort(key=lambda obj: obj.get_nome())
        return favorecido
    
    @staticmethod
    def listar_id_favorecido(id):
        return FavorecidoDAO.listar_id(id)
    
    @staticmethod
    def inserir_favorecido(nome, email, fone, senha):
        favorecido = Favorecido(0, nome, email, fone, senha)
        FavorecidoDAO.inserir(favorecido)

    @staticmethod
    def atualizar_favorecido(id, nome, email, fone, senha):
        favorecido = Favorecido(id, nome, email, fone, senha)
        FavorecidoDAO.atualizar(favorecido)

    @staticmethod
    def excluir_favorecido(id):
        favorecido = Favorecido(id, "", "", "", "")
        FavorecidoDAO.excluir(favorecido)

    @staticmethod
    def autenticar_favorecido(email, senha):
        for favorecido in FavorecidoView.listar_favorecido():
            if favorecido.get_email() == email and favorecido.get_senha() == senha:
                return {"id": favorecido.get_id(), "nome": favorecido.get_nome()}
        return None


class DoadorView:
    @staticmethod
    def listar_doador():
        doador = DoadorDAO.listar()
        doador.sort(key=lambda obj: obj.get_nome())
        return doador
    
    @staticmethod
    def listar_id_doador(id):
        return DoadorDAO.listar_id(id)
    
    @staticmethod
    def inserir_doador(nome, email, senha, cpf, telefone):
        doador = Doador(0, nome, email, senha, cpf, telefone)
        DoadorDAO.inserir(doador)

    @staticmethod
    def atualizar_doador(id, nome, email, senha, cpf, telefone):
        doador = Doador(id, nome, email, senha, cpf, telefone)
        DoadorDAO.atualizar(doador)

    @staticmethod
    def excluir_doador(id):
        doador = Doador(id, "", "", "", "", "")
        DoadorDAO.excluir(doador)

    @staticmethod
    def autenticar_doador(email, senha):
        for doador in DoadorView.listar_doador():
            if doador.get_email() == email and doador.get_senha() == senha:
                return {"id": doador.get_id(), "nome": doador.get_nome()}
        return None


