from database import BancoDeDados
from model.doacao_produto import Produto

class ProdutoDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao VARCHAR(50) NOT NULL,
            tipo VARCHAR(50) NOT NULL,
            quantidade INTEGER NOT NULL,
            id_favorecido INTEGER NOT NULL,
            FOREIGN KEY (id_favorecido) REFERENCES favorecido (id_usuario) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)


    def listar_produto(self):
        comando = "SELECT id, nome, categoria FROM produto;"
        linha = self.__banco_dados.buscar(comando)

        lista_produtos = []

        for id, descricao, categoria, quantidade, id_favorecido in linha:
            lista_produtos.append(Produto(
                id = id
                descricao = descricao
                categoria = categoria
                quantidade = quantidade
                id_favorecido = id_favorecido
            ))

    def listar_id_produto():
        pass

    def inserir_produto(self, produto: Produto):
        comando = "INSERT INTO produto (descricao, categoria, quantidade) VALUES (?, ?, ?);"
        parametros = (produto.descricao, produto.tipo, produto.quantidade)
        self.__banco_dados.executar(comando, parametros)

    def atualizar_produto():
        pass

    def excluir_produto():
        pass