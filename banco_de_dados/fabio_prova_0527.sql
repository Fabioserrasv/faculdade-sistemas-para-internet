--1
SELECT * 
FROM empregados 
WHERE sexo = 'M' AND
salario > 3000 AND
nomeempr LIKE '%jose%';

--2
SELECT nomedepto, nomeempr 
FROM empregados E, departamentos D
WHERE E.matricula = D.matriculager;

--3
SELECT E.nomeempr, COUNT(D.matricula) 
FROM empregados E, dependentes D
WHERE E.matricula = D.matricula
GROUP BY nomeempr;

--4
SELECT E.nomeempr
FROM empregados E
WHERE E.matricula NOT IN(SELECT matricula FROM dependentes);

--5
SELECT AVG(salario)
FROM empregados
WHERE sexo = 'F';]


--6
SELECT SUM(E.salario)
FROM empregados E, trabalha_em T, projetos P
WHERE E.matricula = T.matricula AND 
T.numproj = P.numproj AND 
P.nomeproj = 'Zeus'

--7

SELECT SUM(E.salario)
FROM empregados E
WHERE (SELECT matricula FROM dependentes WHERE matricula = E.matricula) > 1;

--8

SELECT E.nomeempr, E.salario
FROM empregados E, trabalha_em T, projetos P
WHERE E.matricula = T.matricula AND 
T.numproj = P.numproj AND 
P.nomeproj = 'Medusa' AND 
T.horas > 25

--9
SELECT * FROM (SELECT P.numproj, P.nomeproj
FROM empregados E, trabalha_em T, projetos P
WHERE E.matricula = T.matricula AND 
T.numproj = P.numproj AND 
E.nomeempr = 'Pedro Dantas') x WHERE x.numproj IN(SELECT P.numproj
FROM empregados E, trabalha_em T, projetos P
WHERE E.matricula = T.matricula AND 
T.numproj = P.numproj AND 
E.nomeempr = 'Paula de Queiroz')

--10
SELECT DISTINCT E.nomeempr
FROM empregados E, trabalha_em T, projetos P, departamentos DE
WHERE E.matricula = T.matricula AND 
T.numproj = P.numproj AND 
DE.coddepto = P.coddepto AND 
DE.nomedepto = 'Desenvolvimento de Software'