from database import BancoDeDados
from model.usuarios import Usuario

class UsuarioDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(60) NOT NULL
        );
        """
        self.__banco_dados.executar(comando)


    def listar_usuario(self):
        comando = "SELECT id, nome, email, senha FROM usuario;"

    # def buscar(self, comando, parametros=None):
    #     if parametros:
    #         self.__cursor.execute(comando, parametros)
    #     else:
    #         self.__cursor.execute(comando)
    #     return self.__cursor.fetchall()
        linhas = self.__banco_dados.buscar(comando)

        lista_usuarios = []

        for id, nome, email, senha in linhas:
            lista_usuarios.append(Usuario(
                id = id,
                nome = nome,
                email = email
                senha = senha
            ))
        return lista_usuarios


    def listar_id_usuario(self, id):
        comando = """
        SELECT id, nome, email, senha FROM usuario WHERE id = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id,))
        # caso n haja linhas com esse id
        if not linhas:
            return None
        id, nome, email, senha = linhas[0]
        return Usuario(id, nome, email, senha)


    def inserir_usuario(self, usuario: Usuario):
        comando = """
        INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?);
        """
        parametros = (usuario.get_nome(), usuario.get_email(), usuario.get_senha())
        self.__banco_dados.executar(comando, parametros)


    def atualizar_usuario(self, usuario: usuario):
        comando = """
        UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?;
        """
        parametros = (
            usuario.get_nome(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_id()
            )
        self.__banco_dados.executar(comando, parametros)


    def excluir_usuario(self, id):
        comando = """DELETE FROM usuario WHERE id = ?;"""   
        # o método EXECUTAR precisa receber os parametros como tupla
        self.__banco_dados.executar(comando, (id,))