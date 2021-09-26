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
-- Table structure for table `consulta`
--

DROP TABLE IF EXISTS `consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consulta` (
  `idconsulta` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `idpaciente` int NOT NULL,
  `idusolen` int DEFAULT '0',
  `proximacita` date DEFAULT '0000-00-00',
  `idestudiante` int DEFAULT '0',
  `dnp` varchar(20) DEFAULT '0',
  `dnp1` varchar(20) DEFAULT '0',
  `dnp2` varchar(20) DEFAULT '0',
  `dnp3` varchar(20) DEFAULT '0',
  `ultimaevmes` int DEFAULT '0',
  `ultimaevanio` int DEFAULT '0',
  `tiempolen` varchar(20) DEFAULT '0',
  `add1` varchar(20) DEFAULT '0',
  `add2` varchar(20) DEFAULT '0',
  `add3` varchar(20) DEFAULT '0',
  `add11` varchar(20) DEFAULT '0',
  `add22` varchar(20) DEFAULT '0',
  `add33` varchar(20) DEFAULT '0',
  `add111` varchar(20) DEFAULT '0',
  `add222` varchar(20) DEFAULT '0',
  `add333` varchar(20) DEFAULT '0',
  `add1111` varchar(20) DEFAULT '0',
  `add2222` varchar(20) DEFAULT '0',
  `add3333` varchar(20) DEFAULT '0',
  `ojoambliopia` int DEFAULT '0',
  `emetropia` int DEFAULT '0',
  `antimetropia` int DEFAULT '0',
  `tipoametropia` int DEFAULT '0',
  `anisometropia` int DEFAULT '0',
  `patologiaocular` varchar(200) DEFAULT '0',
  `lentesoftalmicos` int DEFAULT '0',
  `lentescontacto` int DEFAULT '0',
  `refoftalmologica` int DEFAULT '0',
  `farmaco` int DEFAULT '0',
  `aprobado` int DEFAULT '0',
  `iduser` int DEFAULT '0',
  `motivoconsulta` varchar(1000) DEFAULT NULL,
  `tipoametropiaoi` int DEFAULT '0',
  `referenciaoftal` varchar(1000) DEFAULT '0',
  PRIMARY KEY (`idconsulta`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consulta`
--

LOCK TABLES `consulta` WRITE;
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` VALUES (6,'2021-09-13',4,1,'2022-09-20',0,'29/29mm','28/28mm','0','0',0,2019,'5 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'CJAlrg+ folículos OU++',1,0,0,1,1,1,'Ref. hace 2 semanas presenta orador pizcazon , y desea cambiar lentes actuales.',0,'0'),(9,'2021-09-13',7,2,'2022-03-15',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,1,2,'0',0,'0'),(10,'2021-09-14',8,1,'2022-03-18',0,'29/29mm','29/29MM','0','0',0,2020,'8 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,1,'0',1,0,0,0,1,1,'Ref. Ardor ocular , desea rectificar RX ACTUAL.',0,'0'),(11,'2021-09-14',9,1,'2022-09-19',0,'34/33mm','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',2,0,0,6,1,'0',1,0,0,0,1,1,'0',0,'0'),(12,'2021-09-14',10,1,'2022-03-19',0,'28/30mm','0','0','0',0,0,'3 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Ref desea rectificar RX actual para cambio de lentes ',0,'0'),(13,'2021-09-16',11,1,'2022-03-18',0,'28/30mm','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'Fotofobia',1,0,0,0,1,1,'Refe. Dolor de cabeza frontal de hace 4 meses inicio,  le cuesta ver un poco de lejos.',0,'0'),(14,'2021-09-16',12,1,'2022-09-19',0,'30/30mm','0','0','0',0,0,'1 ra evaluación','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,1,'0',1,0,0,0,1,1,'Referiere desea evaluar su visión por mala AV',0,'0'),(15,'2021-09-17',13,1,'2022-03-19',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,1,1,1,'Prueba',0,'0'),(16,'2021-09-17',14,1,'2022-03-25',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'Queratocono',0,0,1,1,1,1,'0',0,'0'),(17,'2021-09-17',15,0,'0000-00-00',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,0,0,'0',0,'0'),(18,'2021-09-17',16,1,'2022-09-19',0,'30/32mm','30/32mm','0','0',0,2020,'15 AÑOS','0','0','0','0','0','0','0','0','0','0','0','0',1,0,0,6,1,'0',1,0,0,0,1,1,'Refire desea rectificar la graduación, y pasa todo el dia frente la compu, ha tenido cefalea frontal moderado, ador y picazón, mala AV CON RX ACTUAL. ',0,'0'),(19,'2021-09-17',17,1,'2022-09-19',0,'30/33mm','30/33mm','0','0',0,2020,'6 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'FOTOFOBIO Y CUNJUNTIVITIS POST COVID',1,0,0,0,1,1,'Ref. cuando se desvela siente ardor ocular y cansacio visual. y chequeo anual.',0,'0'),(20,'2021-09-18',18,1,'2022-09-20',0,'30/33mm','0','0','0',0,2018,'5 a 6 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,1,'0',1,0,0,0,1,1,'Ref. usa lentes hace como hace 2 meses sufrio un accidente quebró los lentes, desea reponerlos y rectificar la gradicion.',0,'0'),(21,'2021-09-18',19,1,'2022-09-20',0,'29/33mm','29/33mm','0','0',0,2020,'11 años ','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Ref desea reponer lentes, los quebró hace 2 meses, y desean reponerlos y rectificar la graduación.',0,'0'),(22,'2021-09-18',20,1,'2022-03-25',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'HIPEREMIA COJUNTIVAL FOLICULOS',0,1,0,1,1,1,'LC',0,'0'),(23,'2021-09-18',21,1,'2022-03-20',0,'28/28mm','0','0','0',0,2017,'4 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,1,'0',1,0,0,0,1,1,'Ref, hace 4 años se evaluó, se le recomendaron lentes pero los extravío y los perdió hace 3 años sin lentes. ',0,'0'),(24,'2021-09-18',22,1,'2022-03-20',0,'30/32mm','30/31mm','0','0',0,2020,'7 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,1,'0',1,0,0,0,1,1,'Ref. quebro sus lentes y desea reponerlos y rectificar la graduación. le lloran los ojo , le amanece con celes , inicio hace 4 meses.',0,'0'),(25,'2021-09-20',23,0,'0000-00-00',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,0,0,'0',0,'0'),(26,'2021-09-20',24,1,'2022-09-22',0,'0','27/29mm','0','0',0,2019,'3 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Refieren desean reponer lentes y rectificar la graduación por perdidas.',0,'0'),(27,'2021-09-20',25,1,'2022-09-22',0,'30/29mm','0','0','0',0,2019,'3 AÑOS','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Papa ref desea rectificar la graduación actual para cambio de lentes.',0,'0'),(28,'2021-09-20',26,1,'2022-09-22',0,'30/31mm','30/31mm','0','0',0,2019,'10 años ','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,7,1,'Ojo seco',1,0,0,1,1,1,'Pt ref desea rectificar la graduación para cambio de lentes.',0,'0'),(29,'2021-09-21',27,1,'2022-09-23',0,'31/31mm','30/32mm','0','0',0,2020,'2 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,0,'0',1,0,0,0,1,1,'Refiere dolor de cabeza frontal son frecuentes, pasa 14 horas diarias frente a la pc, no refiere mas síntomas.',0,'0'),(30,'2021-09-21',28,1,'2022-09-23',0,'30/32mm','30/32mm','0','0',0,2020,'5 años.','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Refiere mucha picazón en OU, inicio hace 15 días, le lloran los ojos, y desea rectificar.\r\n',0,'0'),(31,'2021-09-21',29,5,'2022-09-23',0,'32/32mm','0','0','0',0,0,'No ha usado lentes ','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,3,0,'OJO SECO',1,0,0,1,1,1,'Pt ref refiere mala AV en visión cercana, es primera evaluación visual, no ha usado lentes. Ardor, picazón he irritación ocular. no se aplica gotas.',0,'0'),(32,'2021-09-21',30,1,'2022-09-23',0,'32/30mm','0','0','0',0,2018,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,1,1,'Ireg NO OU',1,0,1,0,1,1,'Refiere últimamente siente una telilla, se aplico ojo de águila, y se sintió mejor,  desea evaluar, con la RX ACTUAL desea rectificar mala AV Con la misma.',0,'0'),(33,'2021-09-21',31,1,'2022-09-23',0,'30/32mm','0','0','0',0,2019,'11 AÑOS','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'rEF CAMBIO DE GRADUACION Y RECTIFICAION ',0,'0'),(34,'2021-09-21',32,1,'2022-09-23',0,'34/32mm','30/30mm','0','0',0,0,'UL 22 AÑOS','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'Ectasia corneta +OU',1,0,0,1,1,1,'Refiere forza mucho los ojos, se irritan constantemente los ojos, picazón inicio hace unos 6 meses. rectifico de graduación para cambio de lentes, 41 AÑOS NO REFIER SINTOMAS DE PRESBICIA.',0,'0'),(35,'2021-09-22',33,1,'2022-09-24',0,'28/29','28/30','0','0',0,2018,'0','+3.00','0','1.0','+2.75','0','1.25','0','0','0','0','0','0',0,0,0,9,0,'Ojo seco',1,0,0,1,1,1,'Refiere le molestan los lentes y se los tiene que bajar para leer, 6 meses, no refiere síntomas, ardor ocular al leer, desea rectificar la graduación para cambio de lentes.',0,'0'),(36,'2021-09-22',34,1,'2022-09-24',0,'30/32mm','30/32mm','0','0',0,2018,'5 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,7,1,'Ping. NyT +OU',1,0,0,1,1,1,'Refiere desea cambiar de lentes y desea rectificar la graduación. Irritación ocular continuo.',0,'0'),(37,'2021-09-22',35,1,'2022-03-24',0,'0','0','0','0',4,2021,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'GRANULOMA Y NEVUS CONJUNTIVAL',0,0,1,0,1,1,'Refiere malestar en OI presenta hipertermia conjuntival, le pica, no refiere mas síntomas.',0,'0'),(38,'2021-09-22',36,1,'2022-09-15',0,'32/32mm','32/32mm','0','0',8,2020,'1 año','0','0','0','0','0','0','0','0','0','0','0','0',1,0,0,6,1,'0',1,0,0,0,1,1,'Refiere rectificación de graduación para cambio de lentes.',0,'0'),(39,'2021-09-22',37,1,'2022-09-24',0,'29/29mm','29/29mm','0','0',4,2021,'5 meses','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,1,0,'0',1,0,0,0,1,1,'Refiere a su consulta recomendada a los 6 meses. no refiere síntomas \r\n',0,'0'),(40,'2021-09-22',38,2,'2022-09-24',0,'30/30mm','0','0','0',0,2018,'no','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,0,'CJA OU+ /PTERIGION OD N +',1,0,0,1,1,1,'Tiene tiempo de no realizar un examen visual, no le dejaron lentes, pero actualmente, si ha tenido dolor de cabeza INICIARON HACE 6 MESES EN LA CIEN EL DOLOR SON TOLERABLES, irritación SIEMPRE LA MANTIEN CUANDO VE PANTALLAS , dolor ocular ES EN LOS DOS OJOS , OD SE VE UNA PEQUEÑA CARNOSIDAD.',0,'0'),(41,'2021-09-23',39,1,'2022-03-25',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'opacidad en cristalino ',0,0,1,0,1,1,'0',0,'0'),(42,'2021-09-23',40,1,'2022-03-25',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'Espina OI +',0,0,0,0,1,1,'Presenta dolor y mas es ñor la noche y que la carnosidad le molesta. y por las noches le irrita OI NASAL\r\n',0,'0'),(43,'2021-09-23',41,1,'2022-03-25',0,'28/30mm','0','0','0',0,2019,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,0,'0',1,0,0,0,1,1,'Refiere dessa retirar para campo de lentes, leve picazón en OI ',0,'0'),(44,'2021-09-23',42,1,'2022-03-25',0,'28/30mm','0','0','0',0,2020,'5 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,0,'folículos ',1,1,0,1,1,1,'Refiere desea rectificar la graduación pr recomendación a los 6 meses.',0,'0'),(45,'2021-09-23',43,1,'2022-09-25',0,'30/31','30/31mm','0','0',4,2020,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,0,'0',1,0,0,0,1,1,'Refiere desea recitar gradicuin para cambio de lentes, vista cansada y ojos llorosos. 1mes.',0,'0'),(46,'2021-09-23',44,1,'2022-09-25',0,'33/33mm','0','0','0',0,2009,'10 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,9,1,'0',1,0,0,1,1,1,'Refiere pasa mucho tiempo frente a la compu, y desea un chequeo de prevención. mareo. de vez em puedo.',0,'0'),(47,'2021-09-24',45,1,'2022-09-26',0,'29/30mm','29/30mm','0','0',4,2019,'5 años','0','0','0','0','0','0','0','0','0','0','0','0',1,0,0,6,1,'Ojo seco/ Foliculos',1,0,0,1,1,1,'Refiere un poco de reséquela en los ojos, OD se le cerro, se aplico colirio y le amaneció bien, le afecta mucho quitarse los lentes, y le gusta mas estar sin ellos, no refiere mas, ',0,'0'),(48,'2021-09-24',46,1,'2022-09-26',0,'30/30mm','30/30mm','0','0',12,2018,'8 años','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Refiere desea repones lentes y rectificar la graduación. No refiere mas síntomas.',0,'0'),(49,'2021-09-24',47,1,'2022-09-26',0,'30/30mm','30/30mm','0','0',0,2020,'6 AÑOS','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Refiere le molesta la AV Y VE ALGO BORROSO, 1 MES NO REFIERE MAS SINTOMAS',0,'0'),(50,'2021-09-24',48,0,'0000-00-00',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,0,0,'0',0,'0'),(51,'2021-09-24',49,1,'2022-09-26',0,'31/31mm','0','0','0',0,0,'1 ra evlaucion','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,1,'0',1,0,0,0,1,1,'Ref. Mala AV. PRESENTA PICAZON CONTINUO, MALA AV EN VL, INICO HACE 4 AÑOS, CEFALEA FRONTAL.',0,'0'),(52,'2021-09-25',50,1,'2022-03-27',0,'33/33mm','0','0','0',7,2020,'1 año','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,6,0,'Foliculitis OU +',1,0,0,1,1,1,'Rectifico de graduación para cambio de lentes, le molesta la compu, inicio hace 2 1 semana, parpadea constantemente, presenta irritación contutival, no refiere causa aparente.',0,'0'),(53,'2021-09-25',51,1,'2022-09-27',0,'30/30mm','0','0','0',0,2014,'NO USA LENTES ','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,5,0,'0',1,0,0,0,1,1,'Refiere hace años le recetaron lentes, mala AV EN VL 1 mes, pasa mas tiempo frente a la pc',0,'0'),(54,'2021-09-25',52,1,'2022-03-27',0,'0','0','0','0',0,2010,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'PTRIGION N OU++',0,0,1,1,1,1,'Refiere le duele la parte frontal de la cabeza \r\npresenta carnosidad y le provoca mucha picazón no se a placado gotas.\r\nNo mala AV \r\n\r\n',0,'0'),(55,'2021-09-25',53,0,'0000-00-00',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,0,0,'0',0,'0'),(56,'2021-09-25',54,0,'0000-00-00',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,0,'0',0,0,0,0,0,0,'0',0,'0'),(57,'2021-09-25',13,1,'2021-09-16',0,'0','0','0','0',0,0,'0','0','0','0','0','0','0','0','0','0','0','0','0',0,0,0,0,1,'0',0,0,1,0,1,2,'Motivo prueba concatenado',0,'0');
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;
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
