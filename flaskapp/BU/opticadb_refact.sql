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
-- Table structure for table `refact`
--

DROP TABLE IF EXISTS `refact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refact` (
  `idrefact` int NOT NULL AUTO_INCREMENT,
  `idojo` int DEFAULT NULL,
  `idconsulta` int DEFAULT NULL,
  `esfera` varchar(20) DEFAULT '0',
  `cilindro` varchar(20) DEFAULT '0',
  `eje` varchar(20) DEFAULT '0',
  `prisma` varchar(20) DEFAULT '0',
  `avcc1` varchar(20) DEFAULT '0',
  `avcc2` varchar(20) DEFAULT '0',
  PRIMARY KEY (`idrefact`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refact`
--

LOCK TABLES `refact` WRITE;
/*!40000 ALTER TABLE `refact` DISABLE KEYS */;
INSERT INTO `refact` VALUES (1,1,1,'10','-11','12','13','14','0'),(2,2,1,'5','-6','7','8','9','0'),(3,1,2,'9','-10','11','0','12','0'),(4,2,2,'5','-6','7','0','8','0'),(5,1,2,'9','-10','11','0','12','0'),(6,2,2,'5','-6','7','0','8','0'),(7,1,2,'9','-10','11','0','12','0'),(8,2,2,'5','-6','7','0','8','0'),(9,1,3,'5','-6','7','0','8','0'),(10,2,3,'1','-2','3','0','4','0'),(11,1,6,'-0.75','-1','10','0','1.0','0'),(12,2,6,'-0.50','-1.25','180','0','1.0','0'),(13,1,2,'4','-5','6','0','0','0'),(14,2,2,'1','-2','3','0','0','0'),(15,1,7,'4','-5','6','0','0','0'),(16,2,7,'1','-2','3','0','0','0'),(17,1,8,'0','0','0','0','0','0'),(18,2,8,'0','0','0','0','0','0'),(19,1,9,'0','0','0','0','0','0'),(20,2,9,'0','0','0','0','0','0'),(23,1,10,'-1.75','-2.5','175','0','1.0','0'),(24,2,10,'-1.50','-3.5','15','0','0.63','0'),(25,1,13,'0','0','0','0','0','0'),(26,2,13,'0','0','0','0','0','0'),(27,1,14,'0','0','0','0','0','0'),(28,2,14,'0','0','0','0','0','0'),(29,1,12,'0','0','0','0','0','0'),(30,2,12,'0','0','0','0','0','0'),(31,1,11,'0','0','0','0','0','0'),(32,2,11,'0','0','0','0','0','0'),(33,1,15,'0','0','0','0','0','0'),(34,2,15,'0','0','0','0','0','0'),(35,1,18,'N','-5.5','165','0','1.25','0'),(36,2,18,'-0.50','-0.5','30','0','1.25','0'),(37,1,19,'-2.25','-2','180','0','1.0','0'),(38,2,19,'-2.00','-2','10','0','1.25','0'),(39,1,20,'0','0','0','0','0','0'),(40,2,20,'0','0','0','0','0','0'),(41,1,21,'-1.50','-4','180','0','1.0','0'),(42,2,21,'-4.00','-4','180','0','1.0','0'),(43,1,23,'0','0','0','0','0','0'),(44,2,23,'0','0','0','0','0','0'),(45,1,24,'N','-2.5','10','0','0','0'),(46,2,24,'N','-2.5','165','0','0','0'),(47,1,26,'-3.25','-3.5','180','0','0.63','0'),(48,2,26,'-3.50','-4','5','0','0.63','0'),(49,1,26,'-3.25','-3.5','180','0','0.63','0'),(50,2,26,'-3.50','-4','5','0','0.63','0'),(51,1,27,'-2.75','-2.5','165','0','0.5','0'),(52,2,27,'-2.75','-2.75','180','0','0.63','0'),(53,1,28,'+0.50','-1.25','170','0','1.25','0'),(54,2,28,'+0.25','-1.75','5','0','1.25','0'),(55,1,29,'-0.75','0','0','0','0','0'),(56,2,29,'-0.75','-0.25','12','0','0','0'),(57,1,30,'-2.00','-3.5','180','0','0.5','0'),(58,2,30,'-0.75','-3.75','174','0','0.63','0'),(59,1,31,'0','0','0','0','0','0'),(60,2,31,'0','0','0','0','0','0'),(61,1,32,'0','0','0','0','0','0'),(62,2,32,'0','0','0','0','0','0'),(63,1,33,'-13.50','-1.5','155','0','0','0'),(64,2,33,'-8.00','-3','5','0','0','0'),(65,1,34,'-1.25','-5','155','0','0.4','0'),(66,2,34,'-1.25','-4','25','0','0.8','0'),(67,1,35,'+1.50','-0.5','70','0','1.25','0'),(68,2,35,'+1.50','0','0','0','1.25','0'),(69,1,36,'+0.25','-0.5','5','0','0','0'),(70,2,36,'N','0','0','0','0','0'),(71,1,37,'0','0','0','0','0','0'),(72,2,37,'0','0','0','0','0','0'),(73,1,38,'-0.50','-3','165','0','0.12','0'),(74,2,38,'-2.00','-1.75','10','0','0.5','0'),(75,1,39,'-2.25','0','0','0','0.63','0'),(76,2,39,'-2.25','0','0','0','0.63','0'),(77,1,40,'0','0','0','0','0','0'),(78,2,40,'0','0','0','0','0','0'),(79,1,42,'0','0','0','0','0','0'),(80,2,42,'0','0','0','0','0','0'),(81,1,41,'0','0','0','0','0','0'),(82,2,41,'0','0','0','0','0','0'),(83,1,16,'0','0','0','0','0','0'),(84,2,16,'0','0','0','0','0','0'),(85,1,22,'0','0','0','0','0','0'),(86,2,22,'0','0','0','0','0','0'),(87,1,43,'-2.00','-2','180','0','0','0'),(88,2,43,'-2.75','-1.75','15','0','0','0'),(89,1,44,'0','0','0','0','0','0'),(90,2,44,'0','0','0','0','0','0'),(91,1,45,'-2.50','-5','177','0','0','0'),(92,2,45,'-2.50','-7','5','0','0','0'),(93,1,46,'0','0','0','0','0','0'),(94,2,46,'0','0','0','0','0','0'),(95,1,47,'-0.50','-0.5','175','0','0','0'),(96,2,47,'-3.00','-1.5','20','0','0','0'),(97,1,48,'-5.50','-3.5','5','0','0.63','0'),(98,2,48,'-1.00','-3.5','10','0','0.8','0'),(99,1,49,'-1.50','-5.75','180','0','0','0'),(100,2,49,'-3.25','-5.75','5','0','0','0'),(101,1,51,'0','0','0','0','0','0'),(102,2,51,'0','0','0','0','0','0'),(103,1,52,'-0.25','-0.5','180','0','0','0'),(104,2,52,'-0.50','-0.5','180','0','0','0'),(105,1,53,'0','0','0','0','0','0'),(106,2,53,'0','0','0','0','0','0'),(107,1,54,'0','0','0','0','0','0'),(108,2,54,'0','0','0','0','0','0'),(109,1,57,'0','0','0','0','0','0'),(110,2,57,'0','0','0','0','0','0');
/*!40000 ALTER TABLE `refact` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-25 18:06:54
