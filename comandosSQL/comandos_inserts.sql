-- INSERT INTO:
-- insere dentro de uma tabela, nos campos que foram determinados, os valores dados em seguida

INSERT INTO endereco (cep, uf, cidade, bairro, rua, numero, complemento)
VALUES ('11223344', 'RN', 'Natal', 'Candelária', 'Senhor do Bonfim', '20', '1º andar'),
('12121212', 'PB', 'Patos', 'Candelária', 'Senhor do Bonfim', '20', '1º andar'),
('11223344', 'RN', 'Natal', 'Candelária', 'Av. Salgado Filho', '3500', 'Apto 302'),
('33445566', 'RN', 'Parnamirim', 'Nova Parnamirim', 'Rua Abel Cabral', '890', 'Casa'),
('55667788', 'PE', 'Recife', 'Boa Viagem', 'Av. Boa Viagem', '1200', 'Bloco B');

--------------

INSERT INTO usuario (nome, email, senha)
VALUES ('Ana', 'ana@gmail.com', '123456'),
('Bruno', 'bruno@gmail.com', '123456'),
('Carla', 'carla@gmail.com', '123456'),
('Diego', 'diego@gmail.com', '123456'),
('Eduarda', 'eduarda@gmail.com', '123456');

---------------

INSERT INTO admin (id_usuario, cnpj)
VALUES (1, '12345678000101'),
(2, '12345678000102'),
(3, '12345678000103'),
(4, '12345678000104'),
(5, '12345678000105');

----------------

INSERT INTO doador (cpf, telefone)
VALUES ('90991298324', '82909090322'),
('90991298325', '82909090326'),
('90991298327', '82909090327'),
('90991298326', '82909090325'),
('90921298324', '82949090322');

----------------

INSERT INTO favorecido (id_usuario, cpf, telefone, id_endereco)
VALUES (1, '12345678901', '84991234567', 1),
(2, '23456789012', '84992345678', 2),
(3, '34567890123', '84993456789', 3),
(4, '45678901234', '84994567890', 4),
(5, '56789012345', '84995678901', 5);

----------------

INSERT INTO doacao (descricao, tipo, quantidade_doada, quantidade_disponivel, situacao, id_doador)
VALUES ('Computador', 'Eletrônico', 10, 10, 'disponivel', 1),
('Camiseta social', 'Roupa', 25, 20, 'disponivel', 2),
('Cobertores', 'Bem-estar', 15, 5, 'disponivel', 3),
('Mouse', 'Eletrônico', 30, 30, 'disponivel', 4),
('Garrafas de água', 'Bem-estar', 50, 0, 'indisponivel', 5);


-----------------

INSERT INTO produto (descricao, tipo, quantidade, situacao, id_favorecido)
VALUES ('Cadeiras reutilizadas', 'Móvel', 6, 'disponivel', 1),
('Mesas reaproveitadas', 'Móvel', 4, 'disponivel', 2),
('Roupas reformadas', 'Vestuário', 20, 'disponivel', 3),
('Brinquedos consertados', 'Brinquedo', 15, 'disponivel', 4),
('Eletrodomésticos revisados', 'Eletrodoméstico', 3, 'indisponivel', 5);
