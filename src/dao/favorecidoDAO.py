from database import BancoDeDados
from model.usuarios import Favorecido

class FavorecidoDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS favorecido (
            id_usuario INTEGER PRIMARY KEY,
            cpf CHAR(11) NOT NULL UNIQUE,
            id_telefone INTEGER NOT NULL,
            id_endereco INTEGER NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE,
            FOREIGN KEY (id_telefone) REFERENCES telefone (id) ON DELETE CASCADE,
            FOREIGN KEY (id_endereco) REFERENCES endereco (id) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)


    def listar_favorecidos(self):
        comando = "SELECT id_usuario, cpf, id_telefone, id_endereco FROM favorecido;"

        linhas = self.__banco_dados.buscar(comando)

        lista_favorecidos = []
        for id_usuario, cpf, id_telefone, id_endereco in linhas:
            lista_favorecidos.append(Favorecido(id_usuario, cpf, id_telefone, id_endereco))

        return lista_favorecidos


    def buscar_favorecido_por_id(self, id_usuario):
        comando = """
        SELECT id_usuario, cpf, id_telefone, id_endereco FROM favorecido WHERE id_usuario = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id_usuario,))
        # caso n haja linhas com esse id
        if not linhas:
            return None
        id_usuario, cpf, id_telefone, id_endereco = linhas[0]
        return Favorecido(id_usuario, cpf, id_telefone, id_endereco)


    def inserir_favorecido(self, favorecido: Favorecido):
        comando = """
        INSERT INTO favorecido (id_usuario, cpf, id_telefone, id_endereco) VALUES (?, ?, ?, ?);
        """
        parametros = (favorecido.get_id_usuario(), favorecido.get_cpf(), favorecido.get_id_telefone(), favorecido.get_id_endereco())
        self.__banco_dados.executar(comando, parametros)


    def atualizar_favorecido(self, favorecido: Favorecido):
        comando = """
        UPDATE favorecido SET cpf = ?, id_telefone = ?, id_endereco = ? WHERE id_usuario = ?;
        """
        parametros = (favorecido.get_cpf(), favorecido.get_id_telefone(), favorecido.get_id_endereco(), favorecido.get_id_usuario())
        self.__banco_dados.executar(comando, parametros)


    def excluir_favorecido(self, id_usuario):
        comando = """DELETE FROM favorecido WHERE id_usuario = ?;"""   
        # o método EXECUTAR precisa receber os parametros como tupla
        self.__banco_dados.executar(comando, (id_usuario,))