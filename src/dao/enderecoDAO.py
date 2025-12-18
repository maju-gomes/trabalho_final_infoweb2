from database import BancoDeDados
from model.atributos_usuarios import Endereco

class EnderecoDAO:
    def __init__(self, banco_dados : BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS endereco (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cep CHAR(8) NOT NULL,
            uf CHAR(2) NOT NULL,
            cidade VARCHAR(100) NOT NULL,
            bairro VARCHAR(100) NOT NULL,
            rua VARCHAR(150) NOT NULL,
            numero VARCHAR(10) NOT NULL,
            complemento VARCHAR(50) NULL
        );
        """
        self.__banco_dados.executar(comando)

    def listar_enderecos(self):
        comando = """
        SELECT id, cep, uf, cidade, bairro, rua, numero, complemento FROM endereco;
        """
        linhas = self.__banco_dados.buscar(comando)

        lista_enderecos = []
        for id, cep, uf, cidade, bairro, rua, numero, complemento in linhas:
            lista_enderecos.append(Endereco(id, cep, uf, cidade, bairro, rua, numero, complemento))

        return lista_enderecos

    def buscar_endereco_por_id(self, id):
        comando = """
        SELECT id, cep, uf, cidade, bairro, rua, numero, complemento FROM endereco WHERE id = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id,))

        if not linhas:
            return None
        id, cep, uf, cidade, bairro, rua, numero, complemento = linhas[0]
        return Endereco(id, cep, uf, cidade, bairro, rua, numero, complemento)

    def inserir_endereco(self, endereco: Endereco):
        comando = """
        INSERT INTO endereco (cep, uf, cidade, bairro, rua, numero, complemento)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        parametros = (
            endereco.get_cep(), endereco.get_uf(), endereco.get_cidade(), endereco.get_bairro(),
            endereco.get_rua(), endereco.get_numero(), endereco.get_complemento())

        self.__banco_dados.executar(comando, parametros)

    def atualizar_endereco(self, endereco: Endereco):
        comando = """
        UPDATE endereco SET cep = ?, uf = ?, cidade = ?,
        bairro = ?, rua = ?, numero = ?, complemento = ?
        WHERE id = ?;
        """

        parametros = (endereco.get_cep(), endereco.get_uf(), endereco.get_cidade(),
        endereco.get_bairro(), endereco.get_rua(), endereco.get_numero(),
        endereco.get_complemento(), endereco.get_id())

        self.__banco_dados.executar(comando, parametros)

    def excluir_endereco(self, id):
        comando = """
        DELETE FROM endereco WHERE id = ?;
        """
        self.__banco_dados.executar(comando, (id,))

