import sqlite3

class BancoDeDados:
    def __init__(self, banco_dados="banco_dados.db"):
        self.__conexao = sqlite3.connect(banco_dados)
        self.__cursor = self.__conexao.cursor()

    # executa comandos SQL que não retornam dados
    def executar(self, comando, parametros=None):
        if parametros:
            self.__cursor.execute(comando, parametros)
        else:
            self.__cursor.execute(comando)
        self.__conexao.commit()

    # exeecuta comandos SQL que retornam dado   s
    def buscar(self, comando, parametros=None):
        if parametros:
            self.__cursor.execute(comando, parametros)
        else:
            self.__cursor.execute(comando)
        return self.__cursor.fetchall()

    def fechar(self):
        self.__cursor.close()
        self.__conexao.close()