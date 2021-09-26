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
-- Table structure for table `antmed`
--

DROP TABLE IF EXISTS `antmed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antmed` (
  `idantmed` int NOT NULL AUTO_INCREMENT,
  `idantecedentes` int DEFAULT NULL,
  `enfermedad` varchar(150) DEFAULT NULL,
  `otro` varchar(150) DEFAULT NULL,
  `tiempoevolucion` varchar(150) DEFAULT NULL,
  `control` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idantmed`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `antmed`
--

LOCK TABLES `antmed` WRITE;
/*!40000 ALTER TABLE `antmed` DISABLE KEYS */;
INSERT INTO `antmed` VALUES (1,1,'Diabetes Mellitus',NULL,'0','0'),(2,1,'0',NULL,'0','0'),(3,2,'0',NULL,'0','0'),(4,2,'0',NULL,'0','0'),(5,2,'0',NULL,'0','0'),(6,3,'Otro','Cancer','2 meses','Quimioterapia'),(7,4,'Otro','0','0','0'),(8,4,'Diabetes Mellitus','0','0','0'),(9,2,'0','0','0','0'),(10,5,'0','0','0','0'),(11,6,'0','0','0','0'),(12,7,'0','0','0','0'),(14,9,'0','0','0','0'),(15,10,'0','0','0','0'),(16,11,'0','0','0','0'),(17,12,'0','0','0','0'),(18,13,'0','0','0','0'),(19,14,'0','0','0','0'),(20,15,'0','0','0','0'),(21,16,'0','0','0','0'),(22,17,'0','0','0','0'),(23,18,'0','0','0','0'),(24,19,'0','0','0','0'),(25,20,'Otro','Prostata ','8 meses','tamulson'),(26,21,'0','0','0','0'),(27,21,'0','0','0','0'),(28,22,'0','0','0','0'),(29,23,'0','0','0','0'),(30,24,'0','0','0','0'),(31,25,'Otro','Ovario poliquistico','6 meses','Medformina.'),(32,26,'0','0','0','0'),(33,27,'0','0','0','0'),(34,28,'0','0','0','0'),(35,29,'0','0','0','0'),(36,30,'Hipertensión Arterial','0','Controlada','0'),(37,31,'0','0','0','0'),(38,32,'0','0','0','0'),(39,33,'0','0','0','0'),(40,34,'0','0','0','0'),(41,35,'Otro','ovario poliquistico','1 año','Acrea'),(42,36,'0','0','0','0'),(43,37,'0','0','0','0'),(44,38,'0','0','0','0'),(45,39,'0','0','0','0'),(46,40,'0','0','0','0'),(47,41,'0','0','0','0'),(48,42,'0','0','0','0'),(49,43,'0','0','0','0'),(50,44,'0','0','0','0'),(51,45,'0','0','0','0'),(52,46,'0','0','0','0'),(53,47,'0','0','0','0'),(54,48,'0','0','0','0'),(55,49,'0','0','0','0'),(56,50,'0','0','0','0'),(57,14,'0','0','0','0');
/*!40000 ALTER TABLE `antmed` ENABLE KEYS */;
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
