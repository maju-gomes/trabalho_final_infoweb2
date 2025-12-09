from database import BancoDeDados
from model.doacao_doacao import Doacao

class DoacaoDAO:
    def __init__(self, banco_dados: BancoDeDados):
        # aqui criamos um objeto banco_dados para utilizarmos seus métodos
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS doacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao VARCHAR(50) NOT NULL,
            tipo VARCHAR(50) NOT NULL,
            qntd INTEGER NOT NULL,
            id_doador INTEGER NOT NULL,
            FOREIGN KEY (id_doador) REFERENCES doador (id_usuario) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)

    def listar_doacao():
        comando = "SELECT id, descricao, tipo, qntd, id_doador FROM doacao;"

        linhas = self.__banco_dados.buscar(comando)

        lista_doacoes = []

        for id, descricao, tipo, qntd, id_doador in linhas:
            lista_doacoes.append(doacao(
                id = id,
                descricao = descricao,
                tipo = tipo,
                qntd = qntd,
                id_doador = id_doador
            ))

        return lista_doacoes

    def listar_id_doacao(self, id):
        comando = """
        SELECT id, descricao, tipo, qntd, id_doador FROM doacao WHERE id = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id,))

        if not linhas:
            return None

        id, descricao, tipo, qntd, id_doador = linhas[0]
        return Doacao(id, descricao, tipo, qntd, id_doador)

    def inserir_doacao(self, doacao: Doacao):
        comando = """
        INSERT INTO produto (descricao, tipo, qntd, id_doador) VALUES (?, ?, ?, ?);
        """
        parametros = (produto.get_descricao(), produto.get_tipo(), produto.get_qntd(), produto.get_id_doador())
        self.__banco_dados.executar(comando, parametros)

    def atualizar_doacao():
        comando = """
        UPDATE produto SET descricao = ?, tipo = ?, qntd = ?, id_doador = ? WHERE id = ?;
        """
        parametros = (
            produto.get_descricao(),
            produto.get_tipo(),
            produto.get_qntd(),
            produto.get_id_doador(),
            produto.get_id()
            )
        self.__banco_dados.executar(comando, parametros)

    def excluir_doacao():
        comando = "DELETE FROM produto WHERE id = ?;"
        self.__banco_dados.executar(comando, (id,))