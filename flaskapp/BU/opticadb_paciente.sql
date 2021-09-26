-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: opticadb
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `idpaciente` int NOT NULL AUTO_INCREMENT,
  `nombre1` varchar(45) NOT NULL,
  `nombre2` varchar(45) DEFAULT NULL,
  `apellido1` varchar(45) NOT NULL,
  `apellido2` varchar(45) DEFAULT NULL,
  `fechanac` date NOT NULL,
  `idsexo` int NOT NULL,
  `profesion` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `cui` varchar(13) DEFAULT NULL,
  `telefono` varchar(15) NOT NULL,
  `telefono2` varchar(45) DEFAULT NULL,
  `ultimaev` date DEFAULT NULL,
  PRIMARY KEY (`idpaciente`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (1,'Kevin','Humberto','Avendaño','Cua','1998-01-21',2,'Optometrista','Zona 3 Quetzaltenango','3518189790901','30914512','0','2021-09-13'),(2,'Prueba','0','Uno','0','2021-09-13',1,'Prueba','Ciudad','1818181811818','87654321','0','2021-09-13'),(3,'Jorge','Manuel','Molina','0','2010-02-15',1,'Estudiante','Ciudad','0','55555555','0','2021-09-13'),(4,'Daniela','Cristina','Chiguil','Perez','2001-09-13',2,'Estudiante','Zona 10 Quetzaltenango','0','59276822','0','2021-09-13'),(5,'Joel','Pedro','Hernandez','Flores','2010-01-15',1,'Estudiante','Ciudad','7896789657896','12345646','12312312','2021-09-13'),(6,'Prueba','Cristina','Chang','Avila','2003-12-15',2,'Optometrista','Ciudad','741852963741','88888888','22222222','2021-09-13'),(7,'Juan','Pedro','Parker','Mendoza','2001-05-14',2,'Apicultor','Ciudad','8888888888888','55555555','66666666','2021-09-13'),(8,'Sofia','del Milagro','Estrada','Ovalle','2003-06-02',2,'Estudiante','Salcaja','00000000000','36123991','0','2021-09-14'),(9,'Yeison','Manuel','Estrada','Ovalle','1993-10-16',1,'Estudiante','Salcaja','2457977260902','51254069','0','2021-09-14'),(10,'Helen','Ivone','López','Martínez','1990-04-08',2,'Estudiante','San Cristóbal Totonicapán','2060803280802','41536506','0','2021-09-14'),(11,'Dulce','Yamileth','Manzano','Portocarrero','2006-12-15',2,'Estudiante','4ta calle 0-80 zona 10 Quetgo ','00','48570737','0','2021-09-16'),(12,'Flor','de María ','Ramos','Alvarado','2000-05-06',2,'Estudiante','7ma av 0-03 zona 10 Quetgo.','0000','36074150','0','2021-09-16'),(13,'Allan','David','Avendaño','Cua','1997-05-05',1,'Optometrista','Ciudad','0','512432564165','0','2021-09-17'),(14,'Cristian','Gabriel','Citalán','Rojas','2011-06-06',1,'Estudiante','14 calle 0-52 zona 10 Quetgo.','0','34097600','0','2021-09-17'),(15,'Jose','Miguel','Munguia','Armas','2005-03-05',1,'Estudiante','Quetzaltenango','0','35178568','0','2021-09-17'),(16,'Lorena','Lisbeth','Morales','Morales','1986-12-26',2,'Licenciada en Trabajo Social','26 av. 3-m zona 7 Colonia San Antonio','1634998530924','46571491','0','2021-09-17'),(17,'Luis','Eraldo','Morales','Morales','1996-11-16',1,'Estudiante','26 av. 3-m zona 7 Colonia San Antonio','3383989450924','57223060','0','2021-09-17'),(18,'Rodrigo','Danilo','Huertas','Pardo','1982-06-20',1,'Abogado y Notario ','6ta calle E 4A-21 zona 9 Quetgo','1585966840901','58371160','0','2021-09-18'),(19,'Eybrajan','Jose','Itzep','Pérez','2004-01-29',1,'Estudiante','Palmar Quetgo.','0','32418393','0','2021-09-18'),(20,'Karen','Judith','Tezo','Perez','1998-09-07',2,'Estudiante','Condominio la Arboleda D 5-10','3141651260901','54365710','0','2021-09-18'),(21,'Zamady','Nataly','Reyes','Medina','2009-09-11',2,'Estudiante','Salcaja','0','48027130','0','2021-09-18'),(22,'Moises','Ismael','Barillas','Juanta','1986-01-02',1,'Piloto','7maav 8-76 zona 9 Quetgo','1793437770901','30358021','0','2021-09-18'),(23,'Jeimy','Del Rosario','Garcia','Barrios','1996-10-06',2,'Estudiante','4ta calle 5-50 zona 1 Salcaja','3158616650902','77687138','0','2021-09-20'),(24,'Nataly','Esmeralda','Chang','Godinez','2010-11-09',2,'Estudiante','Canton Barrios Quetgo.','0','50999172','0','2021-09-20'),(25,'Heidy','Aracely','Hernandez','Alfaro','2004-08-31',2,'Estudiante','San Jose Chiquilaja','0','59667369','0','2021-09-20'),(26,'Pedro','Miguel','Arreaga','Mendez','1990-07-28',1,'Diseñador Y Publicista','Zona 7 Quetgo','2621881040920','53109228','0','2021-09-20'),(27,'Kenia','Renata','Santos','Alpibez','2002-10-07',2,'Estudiante','Diagonal 3 7-93 A zona 5','3149537280901','56548416','0','2021-09-21'),(28,'Yajaira','Monserrat','Santos','Alpibez','2005-01-02',2,'Estudiante','Diagonal 3 7-93 A zona 5','0','47207718','0','2021-09-21'),(29,'Angelica','Patricia','Herrera','Sunun','1981-12-08',2,'Ama de Casa','San Felipe','1723261761105','38198479','0','2021-09-21'),(30,'Jose','Maria','Gambori','Rodas','1977-12-25',1,'Perito Contador','San Felipe Retahuleu','1700507850920','42501217','0','2021-09-21'),(31,'Geobany','Manuel','Gramajo ','de Leon','2008-08-07',1,'Estudiante','1ra calle 7a-32 zona 2 salcaja','0','41769980','0','2021-09-21'),(32,'Nester','Geobany','Gramajo ','Rodas','1979-12-26',1,'Perito Contador','Salcaja','1636719940902','41769980','0','2021-09-21'),(33,'Nidia','Hortensia','Pérez','Dominguez','1957-03-18',2,'Ama de Casa','22 av. 14-60 zona 3','2361183900901','59224758','0','2021-09-22'),(34,'Veronica','Francisca','Ajtum','Vasquez','1992-01-11',2,'Auxiliar de Corte','Sector 6 Aldea Santa Rita Salcaja','2089039920902','37603505','0','2021-09-22'),(35,'Yulisa','Abigail','Ordoñez','Ulin','2000-01-06',2,'Estudiante','0 calle diagonal 4 0-21 zona 9 Quetgo.','0','32228268','0','2021-09-22'),(36,'Eduardo','Julian','Vasquez','Perez','2004-03-27',1,'Tejedor','Canton Choqui zona 5','0','44365111','0','2021-09-22'),(37,'Heidy','Liliana','Yax','Gonzalez','2003-12-28',2,'Estudiante','6ta av. 5-54 zona 1 la Esperanza','0','44572093','0','2021-09-22'),(38,'Josély','Catalina','López','Alonzo ','1994-03-18',2,'Fisioterapeuta','Diogonal 15 5-17 zona 5 Quetgo','2448051131301','42535624','0','2021-09-22'),(39,'Rosa','Isabel','Chang','De Cojom','1951-12-24',2,'Ama de casa','Zona 5 Quetgo.','0','45188795','0','2021-09-23'),(40,'Jonathan ','Joaquin','López','Garcia','1986-02-16',1,'Cobrador','4ta av. 2-19 zona 4 Salcaja','2500332320801','59447429','0','2021-09-23'),(41,'Katherine ','Loreny','De Leon','Estrada','2002-08-20',2,'Estudiante','7ma av. 2-46 zona 2 salcaja','2833603050902','48156007','0','2021-09-23'),(42,'Melany','Alexandra','Soloj','Estrada','2003-04-23',2,'Estudiante','Salcaja Quetgo','0','42061737','0','2021-09-23'),(43,'Herman','Pablo','Huitz','Sac','1992-02-23',1,'Ingeniero','9na calle 5-49 zona 2 Quetgo.','2116728660901','40390499','0','2021-09-23'),(44,'Lydia','Rosario','Ochoa','Tax','1984-01-05',2,'Atención al Cliente','13 calle c13-68 zona 10 lote 33 Quetgo','2451856311406','59606939','0','2021-09-23'),(45,'Kandy','Milagro','Escobar','Rivera','1999-06-24',2,'Estudiante','Calle Rodolfo Robles 8-43 zona 1 Quetgo.','2062383200901','56305420','0','2021-09-24'),(46,'Victor','Manuel','Puac','Ramos','2005-10-31',1,'Estudiante','0 av 2-04 zona 7 Quetgo.','0','50627993','0','2021-09-24'),(47,'Miguel','Adolfo','Puac','Ramos','2003-09-12',1,'Estudiante','0 av 2-04 zona 7 Quetgo.','2840957290901','54342015','0','2021-09-24'),(48,'Gabriel','Alejandro','Martinez','0','2007-12-31',1,'Estudiante','9na calle 0-98 zona 1 Quetgo.','0','54491756','0','2021-09-24'),(49,'Jessica','Juanita','Martínez','Calderon','1987-09-15',2,'Maestra Parvularia','9na calle 5-49 zona 2 Quetgo.','2928090260804','54491756','0','2021-09-24'),(50,'Roberto','Alejandro','Calderon','Martínez','2004-09-13',1,'Estudiante','Octava calle 4-16 zona 2 Quetgo','0','40447309','0','2021-09-25'),(51,'Maria','Jose','Calderon','Martínez','2002-10-02',2,'Estudiante','Octava calle 4-16 zona 2 Quetgo','0','40460543','0','2021-09-25'),(52,'Gabriela','0','Roldan','Sosa','1985-08-10',2,'Ama de casa','catorce calle 0-35 zona 8 Quetgo','158596404091','59518381','0','2021-09-25');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-25 18:06:55
