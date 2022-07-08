# --------------------------------------------------------
# Host:                         127.0.0.1
# Database:                     empresa2
# Server version:               5.5.15
# Server OS:                    Win32
# HeidiSQL version:             5.0.0.3272
# Date/time:                    2011-12-02 19:55:47
# --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

# Dumping structure for table empresa2.departamentos
CREATE TABLE IF NOT EXISTS `departamentos` (
  `coddepto` char(3) NOT NULL,
  `nomedepto` varchar(40) NOT NULL,
  `matriculager` char(6) NOT NULL,
  `datainiger` datetime DEFAULT NULL,
  PRIMARY KEY (`coddepto`),
  KEY `matriculager` (`matriculager`),
  CONSTRAINT `departamentos_ibfk_1` FOREIGN KEY (`matriculager`) REFERENCES `empregados` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table empresa2.departamentos: 3 rows
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` (`coddepto`, `nomedepto`, `matriculager`, `datainiger`) VALUES ('001', 'Produção de Dispositivos', '990010', '2002-06-10 00:00:00'), ('002', 'Desenvolvimento de Software', '920123', '1999-04-05 00:00:00'), ('003', 'Artes e Artesanato', '019288', '2003-09-22 00:00:00');
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;


# Dumping structure for table empresa2.dependentes
CREATE TABLE IF NOT EXISTS `dependentes` (
  `matricula` char(6) NOT NULL,
  `nomedep` varchar(45) NOT NULL,
  PRIMARY KEY (`matricula`,`nomedep`),
  CONSTRAINT `dependentes_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `empregados` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table empresa2.dependentes: 22 rows
/*!40000 ALTER TABLE `dependentes` DISABLE KEYS */;
INSERT INTO `dependentes` (`matricula`, `nomedep`) VALUES ('019288', 'Tania Soares Pereira'), ('039929', 'Celia Nunes Araújo'), ('039929', 'Deise Nunes Araújo'), ('039929', 'Marcelo Nunes Araújo'), ('070182', 'Fabio Pontes Gomes'), ('070182', 'Julio Pontes Gomes'), ('070182', 'Marília Pontes Gomes'), ('070182', 'Marta Pontes Gomes'), ('088199', 'Larissa Correa Silva'), ('920123', 'Barbara Fonseca'), ('920123', 'Paulo Fonseca'), ('940283', 'Carla Faria dos Santos'), ('940283', 'Felix Faria dos Santos'), ('950021', 'Fabiana Dantas'), ('950021', 'Talita Reis Dantas'), ('950021', 'Tome Dantas'), ('972937', 'Edgard Nascimento'), ('972937', 'Fatima Fontes Nascimento'), ('990010', 'Andre Ferreira Costa'), ('990010', 'Daniel Ferreira Costa'), ('990010', 'Marta Ferreira Costa'), ('990010', 'Sandra Costa');
/*!40000 ALTER TABLE `dependentes` ENABLE KEYS */;


# Dumping structure for table empresa2.empregados
CREATE TABLE IF NOT EXISTS `empregados` (
  `matricula` char(6) NOT NULL,
  `nomeempr` varchar(45) NOT NULL,
  `CPF` char(11) DEFAULT NULL,
  `datanasc` datetime DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `salario` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table empresa2.empregados: 10 rows
/*!40000 ALTER TABLE `empregados` DISABLE KEYS */;
INSERT INTO `empregados` (`matricula`, `nomeempr`, `CPF`, `datanasc`, `sexo`, `salario`) VALUES ('019288', 'Lucia Maria Pereira', '98643700659', '1977-08-25 00:00:00', 'F', 2800.00), ('039929', 'Joaquim Araujo Neto', '68894345689', '1973-03-16 00:00:00', 'M', 1200.00), ('070182', 'Fernando Gomes', '21557954434', '1967-11-19 00:00:00', 'M', 3500.00), ('080028', 'Paula de Queiroz', '38262950115', '1988-06-05 00:00:00', 'F', 500.00), ('088199', 'João de Souza e Silva', '39743628308', '1980-04-08 00:00:00', 'M', 1000.00), ('920123', 'Maria Jose Fonseca', '72849929347', '1970-01-13 00:00:00', 'F', 4000.00), ('940283', 'Antonio Jose dos Santos', '01098558999', '1981-09-29 00:00:00', 'M', 2500.00), ('950021', 'Pedro Dantas', '83949037253', '1972-10-06 00:00:00', 'M', 3500.00), ('972937', 'Beatriz Fontes', '89764237909', '1979-02-22 00:00:00', 'F', 800.00), ('990010', 'Jose Fernandes Costa', '58299100282', '1965-09-20 00:00:00', 'M', 5000.00);
/*!40000 ALTER TABLE `empregados` ENABLE KEYS */;


# Dumping structure for table empresa2.projetos
CREATE TABLE IF NOT EXISTS `projetos` (
  `numproj` char(4) NOT NULL,
  `nomeproj` varchar(20) NOT NULL,
  `coddepto` char(3) NOT NULL,
  PRIMARY KEY (`numproj`),
  KEY `coddepto` (`coddepto`),
  CONSTRAINT `projetos_ibfk_1` FOREIGN KEY (`coddepto`) REFERENCES `departamentos` (`coddepto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table empresa2.projetos: 6 rows
/*!40000 ALTER TABLE `projetos` DISABLE KEYS */;
INSERT INTO `projetos` (`numproj`, `nomeproj`, `coddepto`) VALUES ('0001', 'Netuno', '001'), ('0002', 'Medusa', '003'), ('0003', 'Mercúrio', '001'), ('0004', 'Eclipse', '002'), ('0005', 'Júpiter', '002'), ('0006', 'Zeus', '001');
/*!40000 ALTER TABLE `projetos` ENABLE KEYS */;


# Dumping structure for table empresa2.trabalha_em
CREATE TABLE IF NOT EXISTS `trabalha_em` (
  `matricula` char(6) NOT NULL,
  `numproj` char(4) NOT NULL,
  `horas` int(11) NOT NULL,
  PRIMARY KEY (`matricula`,`numproj`),
  KEY `numproj` (`numproj`),
  CONSTRAINT `trabalha_em_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `empregados` (`matricula`),
  CONSTRAINT `trabalha_em_ibfk_2` FOREIGN KEY (`numproj`) REFERENCES `projetos` (`numproj`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Dumping data for table empresa2.trabalha_em: 15 rows
/*!40000 ALTER TABLE `trabalha_em` DISABLE KEYS */;
INSERT INTO `trabalha_em` (`matricula`, `numproj`, `horas`) VALUES ('019288', '0002', 20), ('039929', '0001', 20), ('039929', '0003', 20), ('070182', '0001', 25), ('070182', '0006', 15), ('080028', '0004', 20), ('088199', '0004', 20), ('088199', '0005', 20), ('920123', '0005', 20), ('940283', '0003', 20), ('940283', '0006', 10), ('950021', '0004', 10), ('950021', '0005', 30), ('972937', '0002', 40), ('990010', '0001', 20);
/*!40000 ALTER TABLE `trabalha_em` ENABLE KEYS */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
