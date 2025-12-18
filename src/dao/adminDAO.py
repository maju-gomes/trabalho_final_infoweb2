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


    def listar_admins(self):
        comando = "SELECT id_usuario, cnpj FROM admin;"
        linhas = self.__banco_dados.buscar(comando)

        lista_admins = []
        for id_usuario, cnpj in linhas:
            lista_admins.append(Admin(id_usuario, cnpj))

        return lista_admins


    def buscar_admin_por_id(self, id_usuario):
        comando = """
            SELECT id_usuario, cnpj FROM admin WHERE id_usuario = ?;
        """
        linhas = self.__banco_dados.buscar(comando, (id_usuario,))
        if not linhas:
            return None
        id_usuario, cnpj = linhas[0]
        return Admin(id_usuario, cnpj)


    def inserir_admin(self, admin: Admin):
        comando = """
            INSERT INTO admin (id_usuario, cnpj) VALUES (?, ?);
        """
        parametros = (admin.get_id_usuario(), admin.get_cnpj())
        self.__banco_dados.executar(comando, parametros)


    def atualizar_admin(self, admin: Admin):
        comando = """
            UPDATE admin SET cnpj = ? WHERE id_usuario = ?;
        """
        parametros = (admin.get_cnpj(), admin.get_id_usuario())
        self.__banco_dados.executar(comando, parametros)


    def excluir_admin(self, id_usuario):
        comando = """
        DELETE FROM admin WHERE id_usuario = ?;
        """   
        self.__banco_dados.executar(comando, (id_usuario,))