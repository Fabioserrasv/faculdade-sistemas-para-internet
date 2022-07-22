
--Implemente uma VIEW que exiba o nome, valor e nome da categoria dos imóveis que estão para aluguel em Imbituba

CREATE VIEW aluguel_imbituba AS
SELECT I.nome, I.valor, C.nome AS categoria
FROM imovel I
WHERE 
 C.id = I.categoria_id AND
 M.id = I.municipio_id AND
 M.nome = "Imbituba" AND
 I.finalidade = "aluguel";

--Implemente uma STORE PROCEDURE que recebe dois valores (mínimo e máximo) e exiba os imóveis para venda nesta faixa.
--OBS: A lista de imóveis a venda deve vir de uma view especifica de imoveis sendo vendidos.

CREATE VIEW imovel_venda AS SELECT * FROM imovel WHERE finalidade = "venda";

DELIMITER $$
CREATE PROCEDURE imoveis_entre(valor_minimo INT, valor_maximo INT)
   BEGIN
   SELECT * FROM imovel_venda WHERE valor BETWEEN valor_minimo AND valor_maximo;
   END $$
DELIMITER ;

CALL imoveis_entre(10000, 200000);

-- Implemente uma TRIGGER que faça backup em outra tabela dos imóveis que forem excluídos.

CREATE TABLE `imovel_remove_log` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`nome` CHAR(150) NOT NULL COLLATE 'latin1_swedish_ci',
	`descricao` TEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`data_cadastro` DATE NULL DEFAULT NULL,
	`finalidade` CHAR(10) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`dormitorios` TINYINT(4) NULL DEFAULT NULL,
	`area` INT(11) NULL DEFAULT NULL,
	`valor` DECIMAL(10,2) NULL DEFAULT NULL,
	`categoria_id` INT(11) NULL DEFAULT NULL,
	`bairro_id` INT(11) NULL DEFAULT NULL,
	`municipio_id` INT(11) NOT NULL,
	`proprietario_id` INT(11) NOT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci';
DELIMITER $$
CREATE TRIGGER `imovel_after_delete` AFTER DELETE ON `imovel` FOR EACH ROW BEGIN
 INSERT INTO imovel_remove_log(id, nome, descricao, data_cadastro, finalidade, dormitorios, area, valor, categoria_id, bairro_id, municipio_id, proprietario_id)
 VALUES(OLD.id, OLD.nome, OLD.descricao, OLD.data_cadastro, OLD.finalidade, OLD.dormitorios, OLD.area, OLD.valor, OLD.categoria_id, OLD.bairro_id, OLD.municipio_id, OLD.proprietario_id);
END $$
DELIMITER ;

--Modifique o BD de forma que cada proprietário tenha uma coluna com o valor total de seu patrimônio. Cada vez que um imóvel é adicionado, alterado ou
--excluído, o respectivo valor de patrimônio do proprietário deve ser atualizado.

ALTER TABLE `proprietario`
	ADD COLUMN `patrimonio_total` DECIMAL(10,2) NULL DEFAULT 0 AFTER `telefone`;

UPDATE proprietario p SET p.patrimonio_total = (SELECT SUM(valor) FROM imovel i WHERE i.proprietario_id = p.id)

DELIMITER $$
CREATE TRIGGER `imovel_after_insert` AFTER INSERT ON `imovel` FOR EACH ROW BEGIN
	UPDATE proprietario SET patrimonio_total = patrimonio_total + NEW.valor WHERE id = NEW.proprietario_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER `imovel_after_update` AFTER UPDATE ON `imovel` FOR EACH ROW BEGIN
  UPDATE proprietario SET patrimonio_total = patrimonio_total + NEW.valor WHERE id = NEW.proprietario_id;
END$$
DELIMITER ;

DELIMITER $$
DROP TRIGGER `imovel_after_delete`;
CREATE TRIGGER `imovel_after_delete` AFTER DELETE ON `imovel` FOR EACH ROW BEGIN
 INSERT INTO imovel_remove_log(id, nome, descricao, data_cadastro, finalidade, dormitorios, area, valor, categoria_id, bairro_id, municipio_id, proprietario_id)
 VALUES(OLD.id, OLD.nome, OLD.descricao, OLD.data_cadastro, OLD.finalidade, OLD.dormitorios, OLD.area, OLD.valor, OLD.categoria_id, OLD.bairro_id, OLD.municipio_id, OLD.proprietario_id);
 UPDATE proprietario SET patrimonio_total = patrimonio_total - OLD.valor WHERE id = OLD.proprietario_id;
END$$
DELIMITER ;

