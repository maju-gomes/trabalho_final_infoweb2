from model.endereco import Endereco
from dao.database import Database

class EnderecoDAO(Database):
    @classmethod
    def inserir(cls, obj:Endereco):
        cls.abrir()
        comando = """
            INSERT INTO endereco (cep, uf, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        parametros = (obj.get_cep(), obj.get_uf(), obj.get_cidade(), obj.get_bairro(), obj.get_rua(), obj.get_numero(), obj.get_complemento())
        cursor = cls.execute(comando, parametros)
        id = cursor.lastrowid
        obj.set_id(id)
        cls.fechar()
        return id

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = "SELECT * FROM endereco"
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Endereco(id, cep, uf, cidade, bairro, rua, numero, complemento) for (id, cep, uf, cidade, bairro, rua, numero, complemento) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = "SELECT * FROM endereco WHERE id = ?"
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Endereco(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj:Endereco):
        cls.abrir()
        comando = """
            UPDATE endereco SET cep = ?, uf = ?, cidade = ?, bairro = ?, rua = ?, numero = ?, complemento = ? WHERE id = ?
        """
        parametros = (obj.get_cep(), obj.get_uf(), obj.get_cidade(), obj.get_bairro(), obj.get_rua(), obj.get_numero(), obj.get_complemento(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        comando = "DELETE FROM endereco WHERE id = ?"
        cls.execute(comando, (id,))
        cls.fechar()
