-- INSERT INTO:
-- insere dentro de uma tabela, nos campos que foram determinados, os valores dados em seguida
-- Obs.: se formos dar valores a todas as colunas, não é necessário especificá-las

-- insere na tabela endereco 5 registros
-- aqui -- INSERT INTO:
-- insere dentro de uma tabela, nos campos que foram determinados, os valores dados em seguida
-- Obs.: se formos dar valores a todas as colunas, não é necessário especificá-las

-- insere na tabela endereco 5 registros
INSERT INTO endereco (cep, uf, cidade, bairro, rua, numero, complemento) VALUES
('11223344', 'RN', 'Natal', 'Candelária', 'Senhor do Bonfim', '20', '1º andar'),
('12121212', 'PB', 'Patos', 'Candelária', 'Senhor do Bonfim', '20', '1º andar'),
('11223344', 'RN', 'Natal', 'Candelária', 'Av. Salgado Filho', '3500', 'Apto 302'),
('33445566', 'RN', 'Parnamirim', 'Nova Parnamirim', 'Rua Abel Cabral', '890', 'Casa'),
('55667788', 'PE', 'Recife', 'Boa Viagem', 'Av. Boa Viagem', '1200', 'Bloco B');

-- tem 15 registros pq o usuário é herdado pelo admin, doador e favorecido
-- e o id dos 3 deve ser distinto, já que um usuário ou é admin, ou doador ou favorecido
INSERT INTO usuario (nome, email, senha) VALUES
('Ana', 'ana@gmail.com', '123456'),
('Bruno', 'bruno@gmail.com', '123456'),
('Carla', 'carla@gmail.com', '123456'),
('Diego', 'diego@gmail.com', '123456'),
('Eduarda', 'eduarda@gmail.com', '123456'),
('Fernanda', 'fernanda@gmail.com', '123456'),
('Gabriel', 'gabriel@gmail.com', '123456'),
('Helena', 'helena@gmail.com', '123456'),
('Igor', 'igor@gmail.com', '123456'),
('Juliana', 'juliana@gmail.com', '123456'),
('Lucas', 'lucas@gmail.com', '123456'),
('Mariana', 'mariana@gmail.com', '123456'),
('Nathan', 'nathan@gmail.com', '123456'),
('Olivia', 'olivia@gmail.com', '123456'),
('Pedro', 'pedro@gmail.com', '123456');

-- insere na tabela admin 5 registros
INSERT INTO admin (id_usuario, cnpj) VALUES
(1, '12345678901234'),
(2, '12345678901245'),
(3, '12345678901256'),
(4, '12345678901267'),
(5, '12345678901278');

-- insere na tabela doador 5 registros
INSERT INTO doador (id_usuario, cpf, telefone) VALUES
(6, '90991298324', '82909090322'),
(7, '90991298325', '82909090326'),
(8, '90991298327', '82909090327'),
(9, '90991298326', '82909090325'),
(10, '90921298324', '82949090322');

-- insere na tabela favorecido 5 registros
INSERT INTO favorecido (id_usuario, cpf, telefone, id_endereco) VALUES
(11, '12345678901', '84991234567', 1),
(12, '23456789012', '84992345678', 2),
(13, '34567890123', '84993456789', 3),
(14, '45678901234', '84994567890', 4),
(15, '56789012345', '84995678901', 5);

-- insere na tabela doacao 5 registros
INSERT INTO doacao (descricao, tipo, quantidade_doada, quantidade_disponivel, situacao, id_doador) VALUES
('Computador', 'Eletrônico', 10, 10, 'disponivel', 6),
('Camiseta social', 'Roupa', 25, 20, 'disponivel', 7),
('Cobertores', 'Bem-estar', 15, 5, 'disponivel', 8),
('Mouse', 'Eletrônico', 30, 30, 'disponivel', 9),
('Garrafas de água', 'Bem-estar', 50, 0, 'indisponivel', 10);

-- insere na tabela produto 5 registros
INSERT INTO produto (descricao, tipo, quantidade, situacao, id_favorecido) VALUES
('Cadeiras reutilizadas', 'Móvel', 6, 'disponivel', 11),
('Mesas reaproveitadas', 'Móvel', 4, 'disponivel', 12),
('Roupas reformadas', 'Vestuário', 20, 'disponivel', 13),
('Brinquedos consertados', 'Brinquedo', 15, 'disponivel', 14),
('Eletrodomésticos revisados', 'Eletrodoméstico', 3, 'indisponivel', 15);
