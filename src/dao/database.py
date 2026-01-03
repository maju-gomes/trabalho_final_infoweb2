import sqlite3

class Database:
    conn = None
    nome_bd = "reciclagem.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor
    
    @classmethod
    def criar_tabelas(cls):
        cls.execute("""
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
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                senha VARCHAR(60) NOT NULL
            ); 
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS admin (
                id_usuario INTEGER PRIMARY KEY,
                cnpj CHAR(14) NOT NULL UNIQUE,
                FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS doador (
                id_usuario INTEGER PRIMARY KEY,
                cpf CHAR(11) NOT NULL UNIQUE,
                telefone CHAR(11) NOT NULL UNIQUE,
                FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
            ); 
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS favorecido (
                id_usuario INTEGER PRIMARY KEY,
                cpf CHAR(11) NOT NULL UNIQUE,
                telefone CHAR(11) NULL,
                id_endereco INTEGER NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE,
                FOREIGN KEY (id_endereco) REFERENCES endereco (id) ON DELETE CASCADE
            );  
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS doacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(50) NOT NULL,
                tipo VARCHAR(50) NOT NULL,
                qntd INTEGER NOT NULL,
                id_doador INTEGER NOT NULL,
                FOREIGN KEY (id_doador) REFERENCES doador (id_usuario) ON DELETE CASCADE
            ); 
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(50) NOT NULL,
                tipo VARCHAR(50) NOT NULL,
                qntd INTEGER NOT NULL,
                id_favorecido INTEGER NOT NULL,
                FOREIGN KEY (id_favorecido) REFERENCES favorecido (id_usuario) ON DELETE CASCADE
            );    
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()