from dao.dao import DAO
from model.usuarios import Admin

class AdminDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        comando = """
            INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?);
        """
        cls.execute(comando, (obj.get_nome(), obj.get_email(), obj.get_senha()))
        cls.fechar()

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