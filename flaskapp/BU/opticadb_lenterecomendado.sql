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
-- Table structure for table `lenterecomendado`
--

DROP TABLE IF EXISTS `lenterecomendado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lenterecomendado` (
  `idlenterecomendado` int NOT NULL AUTO_INCREMENT,
  `idconsulta` int DEFAULT NULL,
  `tipo` int DEFAULT '0',
  `material` int DEFAULT '0',
  `filtro` int DEFAULT '0',
  `color` int DEFAULT '0',
  `lentedetallado` int DEFAULT NULL,
  PRIMARY KEY (`idlenterecomendado`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lenterecomendado`
--

LOCK TABLES `lenterecomendado` WRITE;
/*!40000 ALTER TABLE `lenterecomendado` DISABLE KEYS */;
INSERT INTO `lenterecomendado` VALUES (1,1,1,4,3,5,4),(2,2,4,4,3,3,9),(3,2,4,4,3,4,5),(4,2,4,4,3,4,6),(5,3,6,3,4,5,7),(6,6,1,2,1,4,8),(7,2,4,3,10,6,7),(8,7,4,1,9,3,6),(9,8,4,4,3,4,1),(10,9,3,4,4,5,11),(12,10,1,2,1,4,15),(13,13,1,2,12,4,15),(14,14,1,2,1,4,15),(15,12,1,2,1,4,15),(16,11,1,2,12,4,15),(17,15,1,3,4,2,15),(18,18,1,2,12,4,15),(19,19,1,2,12,4,15),(20,20,1,2,12,4,15),(21,21,1,2,12,4,15),(22,23,1,2,12,4,15),(23,24,1,2,1,4,15),(24,26,1,2,12,4,15),(25,26,1,2,12,4,15),(26,27,1,2,1,4,15),(27,28,1,2,7,1,15),(28,29,1,2,12,4,15),(29,30,1,2,12,4,15),(30,31,1,2,1,4,15),(31,32,1,4,10,5,15),(32,33,1,2,1,4,3),(33,34,1,2,12,4,15),(34,35,2,2,7,4,15),(35,36,1,2,1,4,15),(36,37,1,1,12,1,13),(37,38,1,2,1,4,15),(38,39,1,2,12,4,15),(39,40,1,2,12,4,15),(40,42,1,2,1,1,13),(41,41,1,1,1,1,13),(42,16,1,1,1,1,13),(43,22,1,2,12,4,15),(44,43,1,2,12,4,15),(45,44,1,2,12,4,15),(46,45,1,2,12,4,15),(47,46,1,2,12,4,15),(48,47,1,2,12,4,15),(49,48,1,2,12,4,15),(50,49,1,2,12,4,15),(51,51,1,2,1,4,15),(52,52,1,2,12,4,15),(53,53,1,2,12,4,15),(54,54,1,2,12,4,15),(55,57,1,4,4,4,4);
/*!40000 ALTER TABLE `lenterecomendado` ENABLE KEYS */;
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
