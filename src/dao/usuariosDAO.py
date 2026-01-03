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
        obj.set_id(id)
        cls.abrir()
        comando = """
            INSERT INTO admin (id_usuario, cnpj) VALUES (?, ?);
        """
        cls.execute(comando, (obj.get_id(), obj.get_cnpj()))
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
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, admin.cnpj 
            FROM usuario 
            JOIN admin ON usuario.id = admin.id_usuario
            WHERE admin.id_usuario = ?
        """
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Admin(*linha) if linha else None
        cls.fechar()
        return obj
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        UsuarioDAO.atualizar(obj)
        comando = """
            UPDATE admin SET cnpj = ? WHERE id_usuario = ?;
        """
        parametros = (obj.get_cnpj(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM usuario WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()


class DoadorDAO(Database):
    @classmethod
    def inserir(cls, obj):
        id = UsuarioDAO.inserir(obj)
        obj.set_id(id)
        cls.abrir()
        comando = """
            INSERT INTO doador (id_usuario, cpf, telefone) VALUES (?, ?, ?);
        """
        cls.execute(comando, (obj.get_id(), obj.get_cpf(), obj.get_telefone()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, doador.cpf, doador.telefone
            FROM usuario
            JOIN doador ON usuario.id = doador.id_usuario
        """
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Doador(id, nome, email, senha, cpf, telefone) for (id, nome, email, senha, cpf, telefone) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, doador.cpf, doador.telefone
            FROM usuario 
            JOIN doador ON usuario.id = doador.id_usuario
            WHERE doador.id_usuario = ?
        """
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Doador(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        UsuarioDAO.atualizar(obj)
        comando = """
            UPDATE doador SET cpf = ?, telefone = ? WHERE id_usuario = ?;
        """
        parametros = (obj.get_cpf(), obj.get_telefone(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM usuario WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()


class FavorecidoDAO(Database):
    @classmethod
    def inserir(cls, obj):
        id = UsuarioDAO.inserir(obj)
        obj.set_id(id)
        cls.abrir()
        comando = """
            INSERT INTO favorecido (id_usuario, cpf, telefone, id_endereco) VALUES (?, ?, ?, ?);
        """
        cls.execute(comando, (obj.get_id(), obj.get_cpf(), obj.get_telefone(), obj.get_id_endereco()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, favorecido.cpf, favorecido.telefone, favorecido.id_endereco
            FROM usuario
            JOIN favorecido ON usuario.id = favorecido.id_usuario
        """
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Favorecido(id, nome, email, senha, cpf, telefone, id_endereco) for (id, nome, email, senha, cpf, telefone, id_endereco) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = """
            SELECT usuario.id, usuario.nome, usuario.email, usuario.senha, favorecido.cpf, favorecido.telefone, favorecido.id_endereco
            FROM usuario 
            JOIN favorecido ON usuario.id = favorecido.id_usuario
            WHERE favorecido.id_usuario = ?
        """
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Favorecido(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        UsuarioDAO.atualizar(obj)
        comando = """
            UPDATE favorecido SET cpf = ?, telefone = ?, id_endereco = ? WHERE id_usuario = ?;
        """
        parametros = (obj.get_cpf(), obj.get_telefone(), obj.get_id_endereco(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        comando = "DELETE FROM usuario WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()