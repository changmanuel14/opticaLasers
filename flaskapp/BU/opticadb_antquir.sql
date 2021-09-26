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
-- Table structure for table `antquir`
--

DROP TABLE IF EXISTS `antquir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antquir` (
  `idantquir` int NOT NULL AUTO_INCREMENT,
  `idantecedentes` int DEFAULT NULL,
  `cirugia` varchar(150) DEFAULT NULL,
  `tiempoevolucion` varchar(150) DEFAULT NULL,
  `control` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idantquir`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `antquir`
--

LOCK TABLES `antquir` WRITE;
/*!40000 ALTER TABLE `antquir` DISABLE KEYS */;
INSERT INTO `antquir` VALUES (1,1,'0','0','0'),(2,1,'0','0','0'),(3,2,'0','0','0'),(4,2,'0','0','0'),(5,2,'0','0','0'),(6,3,'0','0','0'),(7,4,'0','0','0'),(8,2,'0','0','0'),(9,5,'0','0','0'),(10,6,'0','0','0'),(11,7,'0','0','0'),(13,9,'0','0','0'),(14,10,'0','0','0'),(15,11,'0','0','0'),(16,12,'0','0','0'),(17,13,'0','0','0'),(18,14,'0','0','0'),(19,15,'0','0','0'),(20,16,'0','0','0'),(21,17,'0','0','0'),(22,18,'apéndice','1 año','no'),(23,19,'0','0','0'),(24,20,'0','0','0'),(25,21,'0','0','0'),(26,21,'0','0','0'),(27,22,'0','0','0'),(28,23,'0','0','0'),(29,24,'0','0','0'),(30,25,'0','0','0'),(31,26,'Cesarea ','1a y 2 meses','no'),(32,27,'0','0','0'),(33,28,'0','0','0'),(34,29,'0','0','0'),(35,30,'pie por un clavo','3 años','0'),(36,31,'0','0','0'),(37,32,'0','0','0'),(38,33,'0','0','0'),(39,34,'0','0','0'),(40,35,'0','0','0'),(41,36,'0','0','0'),(42,37,'0','0','0'),(43,38,'0','0','0'),(44,39,'0','0','0'),(45,40,'0','0','0'),(46,41,'0','0','0'),(47,42,'0','0','0'),(48,43,'0','0','0'),(49,44,'0','0','0'),(50,45,'0','0','0'),(51,46,'0','0','0'),(52,47,'0','0','0'),(53,48,'0','0','0'),(54,49,'0','0','0'),(55,50,'cesaría ','1 año y 8 meses','0'),(56,14,'0','0','0');
/*!40000 ALTER TABLE `antquir` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-25 18:06:56
