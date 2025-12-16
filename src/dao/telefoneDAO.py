from database import BancoDeDados
from model.atributos_usuarios import Telefone

class TelefoneDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS telefone (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ddd CHAR(2) NOT NULL,
            numero VARCHAR(9) NOT NULL
        );
        """
        self.__banco_dados.executar(comando)

    def listar_favorecidos(self):
        comando = "SELECT id, ddd, numero FROM telefone"
        linhas = self.__banco_dados.buscar(comando)

        lista_telefones = []
        for id, ddd, numero in linhas:
            lista_telefones.append(Telefone(id, ddd, numero))

        return lista_telefones

    def buscar_telefone_por_id(self, id):
        comando = """
        SELECT id, ddd, numero FROM telefone;
        """

        linhas = self.__banco_dados.buscar(comando, (id,))
        if not linhas:
            return None

        id, ddd, numero = linhas[0]
        return Telefone(id, ddd, numero)

    def inserir_telefone(self, telefone: Telefone):
        comando = """
        INSERT INTO favorecido (id, ddd, numero) VALUES (?, ?, ?);
        """
        parametros = (telefone.get_id(), telefone.get_ddd(), telefone.get_numero())
        self.__banco_dados.executar(comandos, parametros)

    def atualizar_telefone(self, telefone: Telefone):
        comando = """
        UPDATE favorecido SET id = ?, ddd = ?, numero = ? WHERE id_usuario
        """

        # AJEITAR ISSO AQUI PQ UM TELEFONE0.1 -  0.*USUARIO