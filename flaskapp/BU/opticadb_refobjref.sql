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
-- Table structure for table `refobjref`
--

DROP TABLE IF EXISTS `refobjref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refobjref` (
  `idrefobjref` int NOT NULL AUTO_INCREMENT,
  `idojo` int DEFAULT NULL,
  `idconsulta` int DEFAULT NULL,
  `esfera` varchar(20) DEFAULT '0',
  `cilindro` varchar(20) DEFAULT '0',
  `eje` varchar(20) DEFAULT '0',
  `prisma` varchar(20) DEFAULT '0',
  `dvertice` varchar(20) DEFAULT '0',
  `avcc` varchar(20) DEFAULT '0',
  PRIMARY KEY (`idrefobjref`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refobjref`
--

LOCK TABLES `refobjref` WRITE;
/*!40000 ALTER TABLE `refobjref` DISABLE KEYS */;
INSERT INTO `refobjref` VALUES (1,1,1,'47','-48','49','50','51','52'),(2,2,1,'41','-42','43','44','45','46'),(3,1,2,'39','-40','41','0','42','43'),(4,2,2,'34','-35','36','0','37','38'),(5,1,2,'40','-41','42','0','43','44'),(6,2,2,'35','-36','37','0','38','39'),(7,1,2,'40','-41','42','0','43','44'),(8,2,2,'35','-36','37','0','38','39');
/*!40000 ALTER TABLE `refobjref` ENABLE KEYS */;
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
