
-- (a) estabelece que o telefone de todos os registros da tabela doador
-- serão atualizados para 84112233445
UPDATE doador 
SET telefone = '84112233445';

-- (b) atualiza a quantidade de doações da doação que possui o
-- atributo tipo como eletrônico, para vinte
UPDATE doacao
SET quantidade_doada = 20
WHERE tipo = 'eletrônico';

-- (c) atualiza os campos dos registros, da tabela doação,
-- que são do tipo eletrônico OU que têm id maior que 3 
UPDATE doacao
SET quantidade_doada = 20
WHERE tipo = 'eletrônico' OR id > 3;

-- (d) atualiza os campos quantidade_doada para 20 e descrição para 'cuidado pessoal'
-- dos registros que possuem o campo tipo = 'roupa'
UPDATE doacao
SET quantidade_doada = 20, descricao = 'cuidado pessoal'
WHERE tipo = 'roupa';

-- (e) atualizas os campos quantidade_disponível dos registros
-- que possuem o campo tipo = 'eletrônico' 
-- para a quantidade_disponível (valor antigo) mais 5.
UPDATE doacao
SET quantidade_disponivel = quantidade_disponivel + 5
WHERE tipo = 'eletrônico';

-- (f) deixa em maiúsculo os campos descricao,
-- tipo e situacao de todos os registros da tabela 
UPDATE doacao
SET descricao, tipo, situacao = UPPER(tipo);

-- (g) deleta todos os registros de uma tabela. observe que
-- este comando é diferente do DROP TABLE, que deleta a tabela em si
DELETE FROM doacao;

-- (h) deleta os registros que possuem o campo tipo = 'eletrônico'
DELETE FROM doacao 
WHERE tipo = 'eletrônico';

-- (i) deleta os registros que possuem os campos tipo = 'eletrônico'
-- e a quantidade = 0.
DELETE FROM produto
WHERE tipo = 'eletrônico' and quantidade = 0;

-- (j) deleta os registros que possuem a mínima quantidade_doada,
-- isto é, aqueles que possuem o menor número
DELETE FROM doacao
WHERE quantidade_doada = (
    SELECT MIN(quantidade_doada) FROM doacao); -- seleciona os registros com menor qntd de doações
    --e converte o comando do parenteses nesse valor
 