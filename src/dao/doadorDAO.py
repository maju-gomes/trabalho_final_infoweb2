from database import BancoDeDados
from model.usuarios import Doador

class DoadorDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS doador (
            id_usuario INTEGER PRIMARY KEY,
            cpf CHAR(11) NOT NULL UNIQUE,
            id_telefone INTEGER NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE,
            FOREIGN KEY (id_telefone) REFERENCES telefone (id) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)


    def listar_doadores(self):
        comando = "SELECT id_usuario, cpf, id_telefone FROM doador;"

        linhas = self.__banco_dados.buscar(comando)

        lista_doadores = []
        for id_usuario, cpf, id_telefone in linhas:
            lista_doadores.append(Doador(id_usuario, cpf, id_telefone))

        return lista_doadores


    def buscar_doador_por_id(self, id_usuario):
        comando = """
        SELECT id_usuario, cpf, id_telefone FROM doador WHERE id_usuario = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id_usuario,))
        # caso n haja linhas com esse id
        if not linhas:
            return None
        id_usuario, cpf, id_telefone = linhas[0]
        return Doador(id_usuario, cpf, id_telefone)


    def inserir_doador(self, doador: Doador):
        comando = """
        INSERT INTO doador (id_usuario, cpf, id_telefone) VALUES (?, ?, ?);
        """
        parametros = (doador.get_id_usuario(), doador.get_cpf(), doador.get_id_telefone())
        self.__banco_dados.executar(comando, parametros)


    def atualizar_doador(self, doador: Doador):
        comando = """
        UPDATE doador SET id_telefone = ? WHERE id_usuario = ?;
        """
        parametros = (doador.get_id_telefone(), doador.get_id_usuario())
        self.__banco_dados.executar(comando, parametros)


    def excluir_doador(self, id_usuario):
        comando = """DELETE FROM doador WHERE id_usuario = ?;"""   
        # o método EXECUTAR precisa receber os parametros como tupla
        self.__banco_dados.executar(comando, (id_usuario,))