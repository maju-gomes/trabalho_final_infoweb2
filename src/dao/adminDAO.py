from database import BancoDeDados
from model.usuarios import Admin

class AdminDAO:
    def __init__(self, banco_dados: BancoDeDados):
        self.__banco_dados = banco_dados

    def criar_tabela(self):
        comando = """
        CREATE TABLE IF NOT EXISTS admin (
            id_usuario INTEGER PRIMARY KEY,
            cnpj CHAR(14) NOT NULL UNIQUE,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
        );
        """
        self.__banco_dados.executar(comando)


    def listar_usuarios(self):
        comando = "SELECT id, nome, email, senha FROM usuario;"
        linhas = self.__banco_dados.buscar(comando)

        lista_usuarios = []
        for id_usuario, cnpj in linhas:
            lista_usuarios.append(Admin(id_usuario, cnpj))

        return lista_usuarios


    def buscar_usuario_por_id(self, id):
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


    def atualizar_usuario(self, usuario: Usuario):
        comando = """
            UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?;
        """
        parametros = (usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_id()
        )
        self.__banco_dados.executar(comando, parametros)


    def excluir_usuario(self, id):
        comando = """DELETE FROM usuario WHERE id = ?;"""   
        self.__banco_dados.executar(comando, (id,))