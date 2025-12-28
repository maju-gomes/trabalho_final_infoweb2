from model.usuarios import Usuario, Admin, Doador, Favorecido
from dao.usuariosDAO import UsuarioDAO, AdminDAO, DoadorDAO, FavorecidoDAO

class UsuarioView:
    def listar_usuario():
        pass
    def listar_id_usuario():
        pass
    def inserir_usuario():
        pass
    def atualizar_usuario():
        pass
    def excluir_usuario():
        pass

class FavorecidoView:
    def listar_favorecido():
        pass
    def listar_id_favorecido():
        pass
    def inserir_favorecido():
        pass
    def atualizar_favorecido():
        pass
    def excluir_favorecido():
        pass

class DoadorView:
    def listar_doador():
        doador = DoadorDAO.listar()
        doador.sort(key=lambda obj: obj.get_nome())
        return doador
    
    def listar_id_doador(id):
        return DoadorDAO.listar_id(id)
    
    def inserir_doador(nome, email, fone, senha):
        doador = doador(0, nome, email, fone, senha)
        DoadorDAO.inserir(doador)

    def atualizar_doador(id, nome, email, fone, senha):
        doador = doador(id, nome, email, fone, senha)
        DoadorDAO.atualizar(doador)

    def excluir_doador(id):
        doador = doador(id, "", "", "", "")
        DoadorDAO.excluir(doador)

    def autenticar_doador(email, senha):
        for doador in DoadorView.listar_doador():
            if doador.get_email() == email and doador.get_senha() == senha:
                return {"id": doador.get_id(), "nome": doador.get_nome()}
        return None