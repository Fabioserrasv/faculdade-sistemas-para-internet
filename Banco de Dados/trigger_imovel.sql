CREATE TABLE `imovel_backup` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`nome` CHAR(150) NOT NULL,
	`descricao` TEXT NULL,
	`data_cadastro` DATE NULL DEFAULT NULL,
	`finalidade` CHAR(10) NULL DEFAULT NULL,
	`dormitorios` TINYINT(4) NULL DEFAULT NULL,
	`area` INT(11) NULL DEFAULT NULL,
	`valor` DECIMAL(10,2) NULL DEFAULT NULL,
	`categoria_id` INT(11) NULL DEFAULT NULL,
	`bairro_id` INT(11) NULL DEFAULT NULL,
	`municipio_id` INT(11) NOT NULL,
	`proprietario_id` INT(11) NOT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

CREATE TRIGGER `imovel_after_delete` AFTER DELETE ON `imovel` FOR EACH ROW BEGIN
	INSERT INTO imovel_backup(nome, descricao, data_cadastro, finalidade, dormitorios, area, valor, categoria_id, bairro_id, municipio_id, proprietario_id) 
	VALUES(OLD.nome, OLD.descricao, OLD.data_cadastro, OLD.finalidade, OLD.dormitorios, OLD.area, OLD.valor, OLD.categoria_id, OLD.bairro_id, OLD.municipio_id, OLD.proprietario_id);
END;
