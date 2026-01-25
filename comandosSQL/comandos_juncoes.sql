--(a)
-- Relaciona os favorecidos com seus respectivos endereços
SELECT u.nome, e.cidade, e.bairro, e.rua
FROM favorecido f
INNER JOIN usuario u ON f.id_usuario = u.id
INNER JOIN endereco e ON f.id_endereco = e.id;

--Relaciona cada doação aos dados do doador responsável por ela
SELECT d.descricao, d.tipo, d.quantidade_doada, do.cpf
FROM doacao d
INNER JOIN doador do ON d.id_doador = do.id_usuario;

--Lista os produtos cadastrados com os nomes dos favorecidos beneficiados
SELECT p.descricao, p.tipo, u.nome
FROM produto p
INNER JOIN favorecido f ON p.id_favorecido = f.id_usuario
INNER JOIN usuario u ON f.id_usuario = u.id;

--------------

-- (b)
--Lista todos os usuários, incluindo os que não são doadores
SELECT usuario.nome, doador.cpf
FROM usuario
LEFT OUTER  JOIN doador ON usuario.id = doador.id_usuario;

--Lista todas as doações, incluindo as que não possuem doador
SELECT doacao.descricao, doador.cpf
FROM doador
RIGHT OUTER JOIN doacao ON doador.id_usuario = doacao.id_doador;

-- (c)
--Lista todos os usuários e todas as doações, mostrando nulo quando não houver correspondência
SELECT usuario.nome, doacao.descricao
FROM usuario
FULL OUTER JOIN doacao ON usuario.id = doacao.id_doador;