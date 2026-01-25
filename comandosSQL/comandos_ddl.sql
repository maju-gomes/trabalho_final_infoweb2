-- cria uma tabela ENDERECO, caso ainda não exista uma
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

-- cria uma tabela USUARIO, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(60) NOT NULL
);

-- cria uma tabela ADMIN, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS admin (
    id_usuario INTEGER PRIMARY KEY,
    cnpj CHAR(14) NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
);

-- cria uma tabela DOADOR, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS doador (
    id_usuario INTEGER PRIMARY KEY,
    cpf CHAR(11) NOT NULL UNIQUE,
    telefone CHAR(11) NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
);

-- cria uma tabela FAVORECIDO, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS favorecido (
    id_usuario INTEGER PRIMARY KEY,
    cpf CHAR(11) NOT NULL UNIQUE,
    telefone CHAR(11) NULL,
    id_endereco INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE,
    FOREIGN KEY (id_endereco) REFERENCES endereco (id)
);

-- cria uma tabela DOACAO, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS doacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    quantidade_doada INTEGER NOT NULL,
    quantidade_disponivel INTEGER NOT NULL
    situacao VARCHAR(15) NULL,
    id_doador INTEGER NULL,
    FOREIGN KEY (id_doador) REFERENCES doador (id_usuario)
);

-- cria uma tabela PRODUTO, caso ainda não exista uma
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    quantidade INTEGER NOT NULL,
    situacao VARCHAR(15) NOT NULL,
    id_favorecido INTEGER NULL,
    FOREIGN KEY (id_favorecido) REFERENCES favorecido (id_usuario)
);