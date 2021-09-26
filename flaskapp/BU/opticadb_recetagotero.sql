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
-- Table structure for table `recetagotero`
--

DROP TABLE IF EXISTS `recetagotero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetagotero` (
  `idrecetagotero` int NOT NULL AUTO_INCREMENT,
  `idconsulta` int DEFAULT NULL,
  `medicamento1` varchar(200) DEFAULT NULL,
  `descripcion1` varchar(1000) DEFAULT NULL,
  `medicamento2` varchar(200) DEFAULT NULL,
  `descripcion2` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`idrecetagotero`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetagotero`
--

LOCK TABLES `recetagotero` WRITE;
/*!40000 ALTER TABLE `recetagotero` DISABLE KEYS */;
INSERT INTO `recetagotero` VALUES (1,6,'Lagricel PF:','0','0','0'),(2,11,'Splash Tears:','Aplicar 1 gota en los dos ojos a cada 8 horas por tiempo indefinido.','0','0'),(3,15,'Alfer Lubri:','APLI. 1 GOTA A/C 12 TI','0','0'),(4,18,'0','0','0','0'),(5,19,'0','0','0','0'),(6,20,'0','0','0','0'),(7,21,'0','0','0','0'),(8,23,'0','0','0','0'),(9,24,'0','0','0','0'),(10,26,'0','0','0','0'),(11,26,'0','0','0','0'),(12,27,'0','0','0','0'),(13,28,'Systane Ultra:','Aplicar a/c 4 XTI','0','0'),(14,29,'0','0','0','0'),(15,30,'0','0','0','0'),(16,31,'Splash Tears:','0','0','0'),(17,32,'0','0','0','0'),(18,33,'0','0','0','0'),(19,34,'Alfer Lubri:','aplicar ac 8 xdi','0','0'),(20,35,'Systante ultra','Aplicar a/c 4 1 gota X TI','0','0'),(21,36,'Splas tears:','A AC 4 H X1M ','0','0'),(22,37,'0','0','0','0'),(23,38,'0','0','0','0'),(24,39,'0','0','0','0'),(25,40,'Splash Tears:','AC 4H XTI','NAPHACEL:','1 GOTA CU.IRRIT'),(26,42,'0','0','0','0'),(27,41,'0','0','0','0'),(28,16,'Referencia a prolasere por posible queratocono','0','0','0'),(29,22,'CLODEX:','APLICAR 1 GOTA EN LOS DOS OJOS A CADA 8 HORAS POR 10 DIAS ','0','0'),(30,43,'0','0','0','0'),(31,44,'CLODEX:','A ACA 8 X7D','0','0'),(32,45,'0','0','0','0'),(33,46,'Splash tears:','0','0','0'),(34,47,'AZ OFTENO','A AC 12 2VAD X 15','SPLASH TEARS:','A AC4H X 1 MES'),(35,48,'0','0','0','0'),(36,49,'0','0','0','0'),(37,51,'0','0','0','0'),(38,52,'AZ OFTENO','AC12 X 15 DIS','SPLASH TEARS:','AC 6 HORAS POR 1 MES'),(39,53,'0','0','0','0'),(40,54,'NAPHACEL','APLI 1 GOTA A CA 12 X1M','SPLAH TEARS:','APLI AC 4 HORAS TI'),(41,57,'0','0','0','0');
/*!40000 ALTER TABLE `recetagotero` ENABLE KEYS */;
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
