from dao.database import Database
from model.usuarios import Usuario, Admin, Doador, Favorecido

class UsuarioDAO(Database):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        comando = """
            INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)
        """
        parametros = (obj.get_nome(), obj.get_email(), obj.get_senha())
        cursor = cls.execute(comando, parametros)
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
        cls.abrir()
        comando = """
            UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?
        """
        parametros = (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM usuario WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()

class AdminDAO(Database):
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
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, admin.cnpj
            FROM usuario
            JOIN admin ON usuario.id = admin.id_usuario
        """
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Admin(id, nome, email, senha, cnpj) for (id, nome, email, senha, cnpj) in linhas]
        cls.fechar()
        return objs
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = """SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, admin.cnpj 
        FROM usuario 
        JOIN admin ON usuario.id = admin.id_usuario
        WHERE admin.id_usuario = ?"""
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Admin(*linha) if linha else None
        cls.fechar()
        return obj
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        comando = """
            UPDATE admin SET cnpj = ? WHERE id_usuario = ?;
        """
        parametros = (obj.get_cnpj(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM admin WHERE id_usuario = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()

# ----------------- FALTA FavorecidoDAO e o DoadorDAO

class FavorecidoDAO(Database):
    @classmethod
    def inserir(cls, obj):
        id = UsuarioDAO.inserir(obj)
        cls.abrir()

        # precisa do JOIN
        comando = """
        """
        cls.execute(comando, (id, obj.get_cpf(),))
        cls.fechar()

    @classmethod
    def listar(cls):
        pass

    @classmethod
    def listar_id(cls, id):
        pass

    @classmethod
    def atualizar(cls, obj):
        pass

    @classmethod
    def excluir(cls, obj):
        pass

# -----------------

class DoadorDAO(Database):
    @classmethod
    def inserir(cls, obj):
        pass

    @classmethod
    def listar(cls):
        pass

    @classmethod
    def listar_id(cls, id):
        pass

    @classmethod
    def atualizar(cls, obj):
        pass

    @classmethod
    def excluir(cls, obj):
        pass
