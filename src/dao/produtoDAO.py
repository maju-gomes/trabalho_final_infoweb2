from database import BancoDeDados
from model.produto_produto import Produto

class ProdutoDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS produto(
            ...
        );
        """
        self.__banco_dados.executar(comando)


    def listar_produto():
        pass

    def listar_id_produto():
        pass

    def inserir_produto(self, produto: Produto):
        comando = "INSERT INTO produto (descricao, tipo, quantidade) VALUES (?, ?, ?);"
        parametros = (produto.self.__descricao, produto.self.__tipo, produto.self.__quantidade)
        self.__banco_dados.executar(comando, parametros)

    def atualizar_produto():
        pass

    def excluir_produto():
        pass