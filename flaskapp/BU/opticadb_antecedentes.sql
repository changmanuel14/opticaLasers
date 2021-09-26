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
-- Table structure for table `antecedentes`
--

DROP TABLE IF EXISTS `antecedentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antecedentes` (
  `idantecedentes` int NOT NULL AUTO_INCREMENT,
  `idpaciente` int NOT NULL,
  `oftalmologicos` varchar(1000) DEFAULT NULL,
  `familiares` varchar(1000) DEFAULT NULL,
  `glaucoma` varchar(1000) DEFAULT NULL,
  `alergicas` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`idantecedentes`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `antecedentes`
--

LOCK TABLES `antecedentes` WRITE;
/*!40000 ALTER TABLE `antecedentes` DISABLE KEYS */;
INSERT INTO `antecedentes` VALUES (1,1,'0','0','0','0'),(2,2,'0','0','0','0'),(3,3,'0','0','0','0'),(4,4,'0','0','0','0'),(5,5,'0','0','0','0'),(6,6,'0','0','0','0'),(7,7,'0','0','0','0'),(9,8,'0','0','0','0'),(10,11,'1 ra Evalucion ','Mama usa lentes','No ','0'),(11,12,'0','0','0','0'),(12,10,'uso irregular de lentes ','0','0','0'),(13,9,'0','0','0','0'),(14,13,'0','0','0','0'),(15,16,'INICIO A USRLOS BIEN HACE 8 AÑOS','familia UL ','0','0'),(16,17,'0','0','0','Refiere hace 20 días sufrio covid y le medicaron mucho, fue hospitalizado, y desarrollo alergias.'),(17,18,'Uso diario ','Fam utiliza lentes. ','0','0'),(18,19,'2 meses sin lentes','0','0','0'),(19,21,'perdio lentes y desea rectificar la rx','Papas y hermanos usan lentes\r\n','0','0'),(20,22,'0','0','0','0'),(21,24,'Perdio los lentes hace 5 dias.','Papa UL','0','0'),(22,25,'Uso irregular de los lentes.','Papa y hermanos usan lentes.','0','0'),(23,26,'Ojo seco controlado ','0','0','0'),(24,27,'uso regular de los lentes.','0','0','0'),(25,28,'uso regular.','Fam UL','0','0'),(26,29,'Primera evaluación. ','0','0','0'),(27,30,'TX por infección en uvea.','Fam Usa lentes ','0','0'),(28,31,'DX ADELGAZAMIENTO DE RETINA','PAPA QUERATOCONO','0','0'),(29,32,'Queratocono OU ','NO','NO','penicilina, '),(30,33,'0','0','0','0'),(31,34,'Uso regular de los lentes. por momentos se los quita para descansar.','0','0','0'),(32,35,'Se evaluó en clínica santa lucia y no le refirieron nada.','0','0','0'),(33,36,'Uso regular ','0','0','0'),(34,37,'Reconsulta 6 meses para completar graduación ','0','0','0'),(35,38,'ya le recomendaron hace tiempo atrás, le recomendaron gotas y paños para aliviar los malestares, compresas calientes.','PapaS UL POR EDAD','0','0'),(36,40,'SE APLICA SPLASH TEARS.','0','0','0'),(37,39,'0','0','0','0'),(38,14,'0','0','0','0'),(39,20,'0','0','0','0'),(40,41,'Quebro sus lentes y desea rectificar','Fam UL','0','Polvo y sol'),(41,42,'0','0','0','0'),(42,43,'0','0','0','0'),(43,44,'Utilizo lentes hace hace 10 años y los dejo de utilizar.','Fam UL','0','0'),(44,45,'Insomnio Post covid. 2 am ','0','0','0'),(45,46,'0','Fam Hermano y mama UL','0','0'),(46,47,'0','0','0','0'),(47,49,'No uso lentes','0','0','0'),(48,50,'uso regular ','Fam USAN LENTES','0','sol'),(49,51,'USO LENTES HACE 7 AÑOS PERO LOS USO POR 2 MESES Y POSTERIORMENTE LOS DEJO DE USAR.','FAM UL PAPAS Y HERMANO','0','0'),(50,52,'No le recetaron lentes ni gotas cuando fue con el oftalmologías','Fam UL ','TIA MATERNA ','Rinitis alrg ++');
/*!40000 ALTER TABLE `antecedentes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-25 18:06:53
