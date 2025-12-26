from dao.dao import DAO
from model.usuarios import Usuario, Admin, Doador, Favorecido

class UsuarioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        comando = """
            INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?);
        """
        cursor = cls.execute(comando, (obj.get_nome(), obj.get_email(), obj.get_senha()))
        id = cursor.lastrowid
        cls.fechar()
        return id

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = "SELECT * FROM usuario"
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Usuario(id, nome, email, senha) for (id, nome, email, senha) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = "SELECT * FROM usuario WHERE id = ?"
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Usuario(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        comando = """
            UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?;
        """
        cls.execute(comando, (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM usuario WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()

class AdminDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        id = UsuarioDAO.inserir(obj)
        cls.abrir()
        comando = """
            INSERT INTO admin (id_usuario, cnpj) VALUES (?, ?);
        """
        cls.execute(comando, (id, obj.get_cnpj()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, admin.cnpj from usuario, admin
            WHERE usuario.id = admin.id_usuario
        """
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Admin(id, nome, email, senha, cnpj) for (id, nome, email, senha, cnpj) in linhas]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = "SELECT * FROM admin WHERE id_usuario = ?"
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Admin(*linha) if linha else None
        cls.fechar()
        return obj
    
    @classmethod
    def atualizar(cls, obj):
        comando = """
            UPDATE admin SET cnpj = ? WHERE id_usuario = ?;
        """
        cls.execute(comando, (obj.get_cnpj(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM admin WHERE id_usuario = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()

class Favorecido(DAO):
    @classmethod
    def inserir(cls, obj):
        id = UsuarioDAO.inserir(obj)
        cls.abrir()
        comando = """
            INSERT INTO admin (id_usuario, cpf, id_telefone) VALUES (?, ?, ?);
        """
        cls.execute(comando, (id, obj.get_cnpj(), ))
        cls.fechar()