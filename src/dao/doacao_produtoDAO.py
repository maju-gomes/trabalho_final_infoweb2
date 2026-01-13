from dao.database import Database
from model.doacao_produto import Doacao, Produto

class DoacaoDAO(Database):
    @classmethod
    def inserir(cls, obj:Doacao):
        cls.abrir()
        comando = """
            INSERT INTO doacao (descricao, tipo, quantidade_doada, quantidade_disponivel, situacao, id_doador) VALUES (?, ?, ?, ?, ?, ?)
        """
        parametros = (obj.get_descricao(), obj.get_tipo(), obj.get_quantidade_doada(), obj.get_quantidade_disponivel(), obj.get_situacao(), obj.get_id_doador())
        cursor = cls.execute(comando, parametros)
        id = cursor.lastrowid
        obj.set_id(id)
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = " SELECT * FROM doacao "
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Doacao(id, descricao, tipo, quantidade_doada, quantidade_disponivel, situacao, id_doador) for (id, descricao, tipo, quantidade_doada, quantidade_disponivel, situacao, id_doador) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = "SELECT * FROM doacao WHERE id = ?"
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Doacao(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj:Doacao):
        cls.abrir()
        comando = """
            UPDATE doacao SET descricao = ?, tipo = ?, quantidade_doada = ?, quantidade_disponivel = ?, situacao = ?, id_doador = ? WHERE id = ?
        """
        parametros = (obj.get_descricao(), obj.get_tipo(), obj.get_quantidade_doada(), obj.get_quantidade_disponivel(), obj.get_situacao(), obj.get_id_doador(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj:Produto):
        cls.abrir()
        comando = "DELETE FROM doacao WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()

# -----------------

class ProdutoDAO(Database):
    @classmethod
    def inserir(cls, obj:Produto):
        cls.abrir()
        comando = """
            INSERT INTO produto (descricao, tipo, quantidade, id_favorecido) VALUES (?, ?, ?, ?)
        """
        parametros = (obj.get_descricao(), obj.get_tipo(), obj.get_quantidade(), obj.get_id_favorecido())
        cursor = cls.execute(comando, parametros)
        id = cursor.lastrowid
        obj.set_id(id)
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        comando = " SELECT * FROM produto "
        cursor = cls.execute(comando)
        linhas = cursor.fetchall()
        objs = [Produto(id, descricao, tipo, quantidade, id_favorecido) for (id, descricao, tipo, quantidade, id_favorecido) in linhas]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        comando = "SELECT * FROM produto WHERE id = ?"
        cursor = cls.execute(comando, (id,))
        linha = cursor.fetchone()
        obj = Produto(*linha) if linha else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj:Produto):
        cls.abrir()
        comando = """
            UPDATE produto SET descricao = ?, tipo = ?, quantidade = ?, id_favorecido = ? WHERE id = ?
        """
        parametros = (obj.get_descricao(), obj.get_tipo(), obj.get_quantidade(), obj.get_id_favorecido(), obj.get_id())
        cls.execute(comando, parametros)
        cls.fechar()

    @classmethod
    def excluir(cls, obj:Produto):
        cls.abrir()
        comando = "DELETE FROM produto WHERE id = ?"
        cls.execute(comando, (obj.get_id(),))
        cls.fechar()