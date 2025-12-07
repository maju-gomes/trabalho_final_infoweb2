from database import BancoDeDados
from model.doacao_doacao import Doacao

class DoacaoDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS doacao(
            ...    
        );
        """
        self.__banco_dados.executar(comando)

    def listar_doacao():
        pass

    def listar_id_doacao():
        pass

    def inserir_doacao(self, doacao: Doacao):
        comando = "INSERT INTO doacao (nome, categoria, quantidade) VALUES (?, ?, ?);"
        parametros = (doacao.self.__descricao, doacao.self.__tipo, doacao.self.__quantidade)
        self.__banco_dados.executar(comando, parametros)

    def atualizar_doacao():
        pass

    def excluir_doacao():
        pass