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
            qntd INTEGER NOT NULL,
            id_favorecido INTEGER NOT NULL,
            FOREIGN KEY (id_favorecido) REFERENCES favorecido (id_usuario) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)

    def listar_produto(self):
        comando = "SELECT id, descricao, tipo, qntd, id_favorecido FROM produto;"

    # def buscar(self, comando, parametros=None):
    #     if parametros:
    #         self.__cursor.execute(comando, parametros)
    #     else:
    #         self.__cursor.execute(comando)
    #     return self.__cursor.fetchall()
        linhas = self.__banco_dados.buscar(comando)

        lista_produtos = []

        for id, descricao, tipo, qntd, id_favorecido in linhas:
            lista_produtos.append(Produto(
                id = id,
                descricao = descricao,
                tipo = tipo,
                qntd = qntd,
                id_favorecido = id_favorecido
            ))
        return lista_produtos

    def listar_id_produto(self, id):
        comando = """
        SELECT id, descricao, tipo, qntd, id_favorecido FROM produto WHERE id = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id,))
        # caso n haja linhas com esse id
        if not linhas:
            return None
        id, descricao, tipo, qntd, id_favorecido = linhas[0]
        return Produto(id, descricao, tipo, qntd, id_favorecido)

    def inserir_produto(self, produto: Produto):
        comando = """
        INSERT INTO produto (descricao, tipo, qntd, id_favorecido) VALUES (?, ?, ?, ?);
        """
        parametros = (produto.get_descricao(), produto.get_tipo(), produto.get_qntd(), produto.get_id_favorecido())
        self.__banco_dados.executar(comando, parametros)

    def atualizar_produto(self, produto: Produto):
        comando = """
        UPDATE produto SET descricao = ?, tipo = ?, qntd = ?, id_favorecido = ? WHERE id = ?;
        """
        parametros = (
            produto.get_descricao(),
            produto.get_tipo(),
            produto.get_qntd(),
            produto.get_id_favorecido(),
            produto.get_id()
            )
        self.__banco_dados.executar(comando, parametros)


    def excluir_produto(self, id):
        comando = """DELETE FROM produto WHERE id = ?;"""   
        # o método EXECUTAR precisa receber os parametros como tupla
        self.__banco_dados.executar(comando, (id,))