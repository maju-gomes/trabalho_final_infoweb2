--(a) seleciona todos os registros da tabela doacao
SELECT * FROM doacao;

-- (b) seleciona os campos tipo de todos os registros da tabela doacao
SELECT tipo FROM produto
WHERE quantidade > 10;

-- (c) seleciona os campos tipo e quantidade doada
-- dos registros que possui id menor que 100
-- e têm o campo tipo = 'pendente';
SELECT tipo, quantidade_doada FROM doacao
WHERE id < 100 and situacao = 'pendente'; 

-- (d) seleciona somento registros em que as quantidade de doação é > 10 
-- e os agrupa por doador pelo id do doador
SELECT id_doador, COUNT(*) AS t_doacoes_p_doador
FROM doacao
WHERE quantidade_doada > 10
GROUP BY id_doador;


-- (e) seleciona todos os registros da tabela doacao 
-- cujo id_doador está na tabela doador (doadores cadastrados)
-- e os agrupa
SELECT * FROM doacao
WHERE id_doador IN
(SELECT id_doador FROM doador);