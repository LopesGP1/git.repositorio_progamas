use bd_longa_vida;
create table tb_plano(
plano char (2) NOT NULL PRIMARY KEY,
descricao  varchar (30),
valor decimal (10,2)
);
create table tb_associado(
plano char (2),
nome varchar (40) not null primary key,
endereco varchar (35),
cidade varchar (20),
estado char (2),
cep char (9),
CONSTRAINT plano_fk  FOREIGN KEY (plano)REFERENCES tb_plano (plano)
);



SELECT * FROM tb_associado INNER JOIN tb_plano  ON tb_associado.plano = tb_plano.plano; #2. Extrair uma relação geral de todos os associados e os planos que eles possuem.

SELECT plano,COUNT(*) AS total_associados
FROM tb_associado
WHERE plano = 'B1';#3. Quantos associados possuem o plano B1?

select tb_associado.nome,tb_plano.plano,tb_plano.valor from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano where tb_plano.plano = 'B1';

select * from tb_associado
 where tb_associado.cidade = 'DIADEMA' or tb_associado.cidade = 'COTIA'; # 5. Quais são os associados que moram em COTIA ou em DIADEMA?
 

 
SELECT plano,COUNT(*) AS total_associados
FROM tb_associado
WHERE plano = 'B1';#3. Quantos associados possuem o plano B1?

select tb_associado.nome,tb_plano.plano,tb_plano.valor,tb_associado.cidade 
from tb_associado 
inner join tb_plano on tb_associado.plano = tb_plano.plano where tb_associado.cidade = 'BARUERI'; #6. Apresente o nome, plano e valor dos associados que moram em BARUERI e possuem o plano M1.


SELECT plano,COUNT(*) AS total_associados
FROM tb_associado
WHERE plano = 'B1';#3. Quantos associados possuem o plano B1?

select tb_associado.nome,tb_plano.plano,tb_plano.valor,tb_associado.cidade 
from tb_associado 
inner join tb_plano on tb_associado.plano = tb_plano.plano where tb_associado.cidade = 'SÃO PAULO\n';
#7. Apresente uma relação com nome, plano e valor de todos os associados residentes em SÃO PAULO

#8. Apresente uma relação completa de todos os campos de ambas as tabelas em que o associado possua SILVA no nome.
select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano where NOME LIKE '%SILVA%';

#9. Devido ao aumento do índice IGPM, a empresa reajustou os valores dos planos básicos em 10%, dos planos
#executivos em 5% e dos planos Máster em 3 %. Atualize os valores na tabela planos.


UPDATE tb_plano
SET valor = 
    CASE 
        WHEN plano = 'B1' THEN 200 * 1.10
        WHEN plano = 'B2' THEN 150 * 1.10
        WHEN plano = 'B3' THEN 100 * 1.10
        WHEN plano = 'E1' THEN 350 * 1.05
        WHEN plano = 'E2' THEN 300 * 1.05
        WHEN plano = 'E3' THEN 250 * 1.05
        WHEN plano = 'M1' THEN 500 * 1.03
        WHEN plano = 'M2' THEN 450 * 1.03
        WHEN plano = 'M3' THEN 400 * 1.03
        ELSE valor
        END
where plano in ('B1', 'B2', 'B3', 'E1', 'E2', 'E3', 'M1', 'M2', 'M3');	


#10. O associado PEDRO JOSE DE OLIVEIRA alterou seu plano de B1 para E3. Faça a devida atualização.
update tb_associado
set plano = 'E3'
where nome = 'PEDRO JOSE DE OLIVEIRA';
SELECT * FROM tb_associado WHERE nome LIKE '%PEDRO%JOSE%OLIVEIRA%';


#11. Quantos associados possuem o plano E3?
SELECT plano,COUNT(*) AS total_associados
FROM tb_associado
WHERE plano = 'E3';

#12.Liste o nome e o valor de todos os associados que possuem os planos B1, E1 e M1. 
select tb_associado.plano, tb_associado.nome,tb_plano.valor,tb_plano.descricao from tb_associado 
inner join tb_plano on tb_associado.plano = tb_plano.plano 
where tb_associado.plano = "b1" or tb_associado.plano = "e1" or tb_associado.plano = "m1";

#13. Quais são os associados que possuem plano do tipo EXECUTIVO, independentemente da categoria ser 1, 2 ou 3? 

select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano where tb_plano.plano like ("e%") ;


#14. Quais são os associados que possuem plano dos tipos Básico e Máster? 
select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano where tb_plano.plano like ("b%") or tb_plano.plano like ("m%") ;


#15. A empresa fechou seu escritório na cidade de SANTO ANDRE e transferiu os cliente para um terceirizado. Remova 
#da tabela associados todos os registros existentes de associados da cidade de SANTO ANDRE
select * from tb_associado where tb_associado.cidade like ("santo%andre"); # nesse cado começa com um delete so que se user ele vai remover os cliente agora so estar selecionado os clientes.

#16. Apresente o nome, plano e valor dos associados que moram em SÃO PAULO e possuem os planos M2 e M3. A 
#listagem deve estar ordenada pelo campo nome. 

select tb_associado.nome,tb_associado.plano,tb_plano.descricao,tb_plano.valor 
from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano 
where tb_associado.plano like ("M2") or  tb_associado.plano like ("M3") and tb_associado.cidade like ("Sao Paulo") ;


#17. Apresente uma listagem completa de todos os campos de ambas as tabelas ordenados por tipo de plano. 

select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano order by tb_associado.plano DESC ;


#18. Faça uma relação geral de todos os associados e planos que eles possuem. A relação deve ser apresentada em ordem 
#ascendente pelo campo tipo de plano e descendente pelo campo de identificação do nome do associado. 

select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano 
order by tb_plano.plano asc, tb_associado.nome desc ;

#19. Apresentar uma relação de todos os associados que não possuem o plano Máster.
select * from tb_associado inner join tb_plano on tb_associado.plano = tb_plano.plano
where tb_associado.plano <> "M1"and tb_associado.plano <> "M2" and tb_associado.plano <> "M3";
 
#20. Apresentar uma listagem em ordem crescente pelo campo nome do associado. Essa listagem deve ser formada pelos 
#campos Nome da tabela associado e Descrição da tabela Planos 
select tb_associado.nome,tb_plano.descricao from tb_associado 
inner join tb_plano on tb_associado.plano = tb_plano.plano order by tb_associado.nome asc;

#21.Apresentar uma listagem dos planos que estão situados na faixa de valores de 300 até 500 
select * from tb_plano where tb_plano.valor >= 300;

#22. Apresentar uma relação contendo: nome,plano, descrição do plano e valor de todos os associados que tenham em 
#seu nome, seja na posição que for, a seqüência AMARAL. 
select tb_associado.nome,tb_associado.plano,tb_plano.descricao,tb_plano.valor 
from tb_associado 
inner join tb_plano on tb_associado.plano = tb_plano.plano 
where tb_associado.nome like ("%amaral%");

#23. Quais associados residem na cidade de DIADEMA? 
select * from tb_associado where tb_associado.cidade like ("diadema%");

#24. O plano do tipo MASTER teve um reajuste de 6%. Atualize na tabela planos os valores das categorias 1, 2 e 3. 

UPDATE tb_plano
SET valor = valor * 1.06
WHERE plano IN ('M1', 'M2', 'M3');

 
 select * from tb_plano where tb_plano.plano like  ("M%");




#25. Quais são os clientes cujo CEP é iniciado com os valores 09?

select * from tb_associado where tb_associado.cep like ("09%");

