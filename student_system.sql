-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: personal-zachdavid-0d3b.i.aivencloud.com    Database: student_system
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '311da543-38b8-11f0-b155-862ccfb0004e:1-15,
327440a0-447a-11f0-8812-862ccfb04f4b:1-15,
6be1d805-cc50-11ef-b2eb-82a800179f22:1-19,
93ac1126-6b76-11f0-8a12-862ccfb02411:1-15,
93ea241e-b96a-11ef-bf82-a6dfc6675181:1-47,
ca13e36f-2768-11f0-b8f8-862ccfb05022:1-15,
d3d08314-57f5-11f0-a9c5-862ccfb00e22:1-15,
ed8a66a3-57de-11f0-8fe3-862ccfb03edf:1-15';

--
-- Table structure for table `College`
--

DROP TABLE IF EXISTS `College`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `College` (
  `code` varchar(8) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `College`
--

LOCK TABLES `College` WRITE;
/*!40000 ALTER TABLE `College` DISABLE KEYS */;
INSERT INTO `College` VALUES ('CASS','College of Arts and Social Studies'),('CCS','College of Computer Studies'),('CEBA','College of Economy, Business, and Accountancy'),('CED','College of Education'),('COET','College of Engineering and Technology'),('CHS','College of Health Sciences'),('CSM','College of Science and Mathematics');
/*!40000 ALTER TABLE `College` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Program`
--

DROP TABLE IF EXISTS `Program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Program` (
  `code` varchar(50) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `college` varchar(8) NOT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `name` (`name`),
  KEY `college` (`college`),
  CONSTRAINT `Program_ibfk_1` FOREIGN KEY (`college`) REFERENCES `College` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Program`
--

LOCK TABLES `Program` WRITE;
/*!40000 ALTER TABLE `Program` DISABLE KEYS */;
INSERT INTO `Program` VALUES ('BAELS','BA English Language Studies','CASS'),('BAFil','BA Filipino','CASS'),('BAPan','BA Panitikan','CASS'),('BASocio','BA Sociology','CASS'),('BEed-Lang','BEEd Language Education','CED'),('BSA','BS Accountancy','CEBA'),('BSBA-Econ','BSBA Business Economics','CEBA'),('BSBA-MM','BSBA Marketing Management','CEBA'),('BSBio-Animal','BS Biology (Animal)','CSM'),('BSCA','BS in Computer Applications','CCS'),('BSCE','BS Civil Engineering','COET'),('BSCerE','BS Ceramics Engineering','COET'),('BSChem','BS Chemistry','CSM'),('BSCpE','BS Computer Engineering','COET'),('BSCS','BS in Computer Science','CCS'),('BSEcon','BS Economics','CEBA'),('BSEd-Bio','BEEd Biology','CED'),('BSEM','BS Mining Engineering','COET'),('BSEntrep','BS Entrepreneuship','CEBA'),('BSHM','BS Hospitality Management','CEBA'),('BSIS','BS in Information Systems','CCS'),('BSIT','BS in Information Technology','CCS'),('BSMarineBio','BS Marine Biology','CSM'),('BSMath','BS Mathematics','CSM'),('BSME','BS Mechanical Engineering','COET'),('BSN','BS in Nursing','CHS'),('BSPhil','BS Philosophy','CASS'),('BSPsych','BS Psychology','CASS'),('BSStat','BS Statistics','CSM'),('BTLEd-HE','BTLEd Home Economics','CED'),('BTVTEd-DraftTech','BTVTEd Drafting Technology','CED');
/*!40000 ALTER TABLE `Program` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student` (
  `id_number` varchar(9) NOT NULL,
  `profile_url` varchar(150) DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `program` varchar(50) DEFAULT NULL,
  `year_level` enum('1','2','3','4') DEFAULT NULL,
  `gender` enum('male','female') NOT NULL,
  PRIMARY KEY (`id_number`),
  KEY `program` (`program`),
  CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`program`) REFERENCES `Program` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES ('2021-0036',NULL,'Andre','Hancock','BSEd-Bio','3','female'),('2021-0042',NULL,'Georgiana','Russell','BAELS','1','male'),('2021-0046',NULL,'Audrey','Arnold','BSPsych','4','male'),('2021-0047',NULL,'Johnny','Hendricks','BAFil','2','male'),('2021-0048',NULL,'Alma','Mccoy','BSBA-MM','','female'),('2021-0049',NULL,'Kelly','Knapp','BSCpE','1','male'),('2021-0052',NULL,'Lillie','Bowen','BSIS','4','male'),('2021-0053',NULL,'Aneesa','Welch','BSBio-Animal','4','female'),('2021-0055',NULL,'Kristina','Manning','BSHM','1','female'),('2021-0065',NULL,'Juliet','Lara','BSEntrep','4','male'),('2021-0069',NULL,'Doris','Lin','BSBA-Econ','3','male'),('2021-0075',NULL,'Pearl','Fernandez','BSEcon','3','male'),('2021-0076',NULL,'Anjali','Nielsen','BEed-Lang','2','female'),('2021-0080',NULL,'Maizie','Parker','BASocio','3','female'),('2021-0085',NULL,'Ayla','Hurst','BSCA','','female'),('2021-0086',NULL,'Rayhan','Perkins','BSBA-Econ','','male'),('2021-0090',NULL,'Leo','Hoffman','BSA','1','male'),('2021-0094',NULL,'Phyllis','Griffith','BSCE','4','male'),('2021-0095',NULL,'Jana','John','BSPhil','1','female'),('2021-0096',NULL,'Idris','Woodward','BSA','4','female'),('2021-0097',NULL,'Phoenix','Steele','BSN','3','male'),('2021-0101',NULL,'Flynn','Blankenship','BTVTEd-DraftTech','3','female'),('2021-0107',NULL,'Aaron','David','BSCA','1','male'),('2021-0113',NULL,'Kelvin','Brooks','BSCerE','4','female'),('2021-0114',NULL,'Edmund','Michael','BSCpE','4','female'),('2021-0115',NULL,'Mckenzie','Drake','BSStat','','male'),('2021-0121',NULL,'Roxanne','Vaughn','BSME','2','female'),('2021-0123',NULL,'Drew','Barry','BSEntrep','2','female'),('2021-0125',NULL,'Milo','Ho','BSMarineBio','3','female'),('2021-0128',NULL,'Hayley','Quinn','BSMath','3','female'),('2021-0129',NULL,'Sophia','Coleman','BSBA-Econ','3','male'),('2021-0135',NULL,'Phoebe','Moses','BSPsych','2','female'),('2021-0137',NULL,'Madeleine','Terrell','BSCpE','3','male'),('2021-0138',NULL,'Christina','Robbins','BAPan','','male'),('2021-0143',NULL,'Agnes','Bowers','BSIS','2','female'),('2021-0145',NULL,'Erin','Mcdonald','BSCS','4','female'),('2021-0148',NULL,'Shayla','Schmidt','BTLEd-HE','3','male'),('2021-0150',NULL,'Katelyn','Wells','BAELS','3','male'),('2021-0156',NULL,'Kieron','Rush','BSBA-Econ','','male'),('2021-0160',NULL,'Julia','Owen','BSN','2','male'),('2021-0167',NULL,'Kurtis','Cline','BSStat','4','male'),('2021-0171',NULL,'James','Beck','BTVTEd-DraftTech','1','female'),('2021-0172',NULL,'Shelby','Baldwin','BSMarineBio','2','female'),('2021-0175',NULL,'Rhodri','Huber','BSBio-Animal','3','male'),('2021-0183',NULL,'Hana','Hernandez','BAFil','1','male'),('2021-0192',NULL,'Oakley','Bond','BAELS','1','female'),('2021-0193',NULL,'Alessandro','Hubbard','BSEcon','3','male'),('2021-0196',NULL,'Alexandre','Grant','BSMarineBio','3','female'),('2021-0197',NULL,'Delores','Mejia','BEed-Lang','3','male'),('2021-0202',NULL,'Reid','Bradshaw','BSCpE','3','female'),('2021-0206',NULL,'Connor','Jensen','BSCerE','3','male'),('2021-0207',NULL,'Aishah','Dotson','BSME','1','male'),('2021-0211',NULL,'Ciaran','West','BSPhil','2','female'),('2021-0213',NULL,'Chelsea','Montgomery','BSCA','','male'),('2021-0219',NULL,'Rebekah','Morgan','BSCE','1','female'),('2021-0221',NULL,'Jimmy','Mccall','BSBA-MM','','female'),('2021-0222',NULL,'Gianluca','Merrill','BASocio','2','female'),('2021-0229',NULL,'Louisa','Garrett','BTVTEd-DraftTech','','female'),('2022-0030',NULL,'Renee','Mejia','BSME','4','female'),('2022-0035',NULL,'Usman','Stanton','BAELS','3','male'),('2022-0038',NULL,'Lyndon','Le','BSME','','female'),('2022-0039',NULL,'Neo','Mayo','BTLEd-HE','1','female'),('2022-0040',NULL,'Lucas','Flores','BSEM','2','male'),('2022-0044',NULL,'Estelle','Gallegos','BTVTEd-DraftTech','4','female'),('2022-0051',NULL,'Cora','Torres','BSBA-Econ','1','male'),('2022-0057',NULL,'Lennox','Holland','BSCA','1','female'),('2022-0058',NULL,'Johnathan','Moyer','BSMath','3','male'),('2022-0062',NULL,'Maisy','Kirby','BSCS','1','male'),('2022-0071',NULL,'Cai','Kline','BSEcon','1','male'),('2022-0077',NULL,'Cayden','Palmer','BSPhil','4','female'),('2022-0092',NULL,'Prince','Myers','BSCA','2','male'),('2022-0093',NULL,'Krishan','Hunt','BTVTEd-DraftTech','1','male'),('2022-0102',NULL,'Savanna','Buckley','BSCE','3','female'),('2022-0106',NULL,'Zac','Kane','BAFil','4','female'),('2022-0108',NULL,'Wilbur','Mcpherson','BSCerE','1','female'),('2022-0110',NULL,'Hafsah','Blevins','BAFil','4','female'),('2022-0117',NULL,'William','Cohen','BSBA-Econ','2','male'),('2022-0122',NULL,'Tamsin','Moran','BSEcon','4','male'),('2022-0126',NULL,'Lacie','Henry','BTLEd-HE','','male'),('2022-0127',NULL,'Mohamed','Wilcox','BSIS','3','male'),('2022-0130',NULL,'Ariana','Pearson','BTLEd-HE','2','male'),('2022-0131',NULL,'Saif','Vang','BSPhil','4','female'),('2022-0133',NULL,'Aqsa','Leach','BSChem','1','female'),('2022-0139',NULL,'Esme','Boyd','BSA','1','female'),('2022-0142',NULL,'Casper','Mclaughlin','BSPsych','','male'),('2022-0151',NULL,'Maxim','Joyce','BSCerE','','male'),('2022-0155',NULL,'Maia','Sanford','BAPan','3','female'),('2022-0157',NULL,'Tina','Kim','BSStat','4','male'),('2022-0162',NULL,'Axel','Levy','BSBA-Econ','2','female'),('2022-0163',NULL,'Amin','Rojas','BSStat','4','male'),('2022-0170',NULL,'Sami','Glass','BSEM','1','male'),('2022-0174',NULL,'Ioan','Sykes','BSCE','','male'),('2022-0181',NULL,'Thea','Jordan','BEed-Lang','','male'),('2022-0182',NULL,'Mason','Merritt','BSIS','4','male'),('2022-0189',NULL,'Rhea','Little','BTLEd-HE','4','male'),('2022-0191',NULL,'Alistair','Shah','BSME','3','male'),('2022-0199',NULL,'Niamh','Holder','BSCA','1','female'),('2022-0200',NULL,'Charlie','Raymond','BSHM','2','male'),('2022-0201',NULL,'Abbey','Clements','BSIT','3','female'),('2022-0214',NULL,'Johnny','Cunningham','BSBA-Econ','1','female'),('2022-0215',NULL,'Marianne','Hunt','BSEntrep','4','male'),('2022-0220',NULL,'Ella','Mcneil','BAELS','4','female'),('2022-0223',NULL,'Flora','Terry','BSN','3','female'),('2022-0227',NULL,'Lisa','Walls','BSPsych','2','female'),('2023-0034',NULL,'Chelsey','Donovan','BSCS','','male'),('2023-0037',NULL,'Michaela','Kemp','BEed-Lang','','female'),('2023-0045',NULL,'Jason','Molina','BSBA-MM','3','female'),('2023-0054',NULL,'Cordelia','Mcguire','BSStat','4','female'),('2023-0056',NULL,'Kyan','Reed','BASocio','1','male'),('2023-0059',NULL,'Yasmine','Sutton','BSEd-Bio','4','female'),('2023-0060',NULL,'Sophie','Mcclure','BSCS','4','male'),('2023-0061',NULL,'Bella','Hahn','BSIT','','male'),('2023-0063',NULL,'Oakley','Robertson','BEed-Lang','3','male'),('2023-0070',NULL,'Skyla','Wallace','BSBA-MM','3','male'),('2023-0072',NULL,'Cain','Stein','BSCS','3','female'),('2023-0078',NULL,'Darragh','Ortiz','BSPhil','2','female'),('2023-0081',NULL,'Lily-Rose','Dean','BSMarineBio','1','male'),('2023-0087',NULL,'Hermione','Bowman','BSME','','female'),('2023-0091',NULL,'Harris','Garrison','BSChem','3','female'),('2023-0098',NULL,'Angelo','Acevedo','BSPhil','3','female'),('2023-0104',NULL,'Mahdi','Wu','BSStat','4','female'),('2023-0116',NULL,'Beatrix','Meyers','BAPan','1','female'),('2023-0119',NULL,'Jazmin','Swanson','BEed-Lang','','female'),('2023-0120',NULL,'Daisy','Price','BAELS','','female'),('2023-0134',NULL,'Yaseen','Alexander','BSBio-Animal','','female'),('2023-0140',NULL,'Bernard','Marquez','BSHM','2','female'),('2023-0141',NULL,'Wilma','Harding','BSME','1','male'),('2023-0159',NULL,'Malik','Finley','BAFil','','female'),('2023-0161',NULL,'Ricky','Harris','BSCpE','2','male'),('2023-0164',NULL,'Connie','Bradford','BSEntrep','','male'),('2023-0165',NULL,'Jeremy','Elliott','BSStat','2','male'),('2023-0168',NULL,'Eliot','Parrish','BSMarineBio','1','female'),('2023-0173',NULL,'Alec','Holt','BSPsych','4','female'),('2023-0178',NULL,'Olive','Mullins','BSMath','2','male'),('2023-0180',NULL,'Clayton','Bolton','BSStat','3','female'),('2023-0185',NULL,'Heather','Khan','BAELS','2','male'),('2023-0187',NULL,'Macie','Kirby','BSCA','1','male'),('2023-0188',NULL,'Safaa','Kane','BTVTEd-DraftTech','2','male'),('2023-0194',NULL,'Miah','Hatfield','BSIT','2','female'),('2023-0198',NULL,'Janet','Holman','BSIS','4','male'),('2023-0203',NULL,'Maizie','Hill','BSMarineBio','1','male'),('2023-0204',NULL,'Estelle','Ali','BSHM','1','female'),('2023-0205',NULL,'Emily','Fuentes','BSChem','1','female'),('2023-0208',NULL,'Ifan','Beltran','BASocio','4','female'),('2023-0212',NULL,'Bill','Cardenas','BTLEd-HE','3','female'),('2023-0217',NULL,'Zahra','Macias','BSIT','4','male'),('2023-0218',NULL,'Tyler','Charles','BSCerE','3','male'),('2023-0224',NULL,'Cody','Weiss','BSME','2','female'),('2023-0225',NULL,'Husna','Gutierrez','BSCS','3','male'),('2024-0031',NULL,'Jessica','Roy','BSEM','','male'),('2024-0032',NULL,'Talia','Craig','BSEntrep','2','male'),('2024-0033',NULL,'Franklin','Mcclain','BSEM','4','female'),('2024-0041',NULL,'Cassius','Kerr','BSBA-MM','4','female'),('2024-0043',NULL,'Ela','Warner','BSPsych','','female'),('2024-0050',NULL,'Blanche','Welsh','BSIS','1','male'),('2024-0064',NULL,'Anton','Schultz','BSCerE','1','female'),('2024-0066',NULL,'Mathew','Henderson','BSEd-Bio','3','female'),('2024-0067',NULL,'Otto','Bright','BSEntrep','3','female'),('2024-0068',NULL,'Anish','Church','BSN','','female'),('2024-0073',NULL,'Ryan','Houston','BSIS','2','male'),('2024-0074',NULL,'Annabella','Bishop','BSBA-MM','4','male'),('2024-0079',NULL,'Clara','Hull','BSStat','','female'),('2024-0082',NULL,'Muhammad','Alexander','BSStat','1','female'),('2024-0083',NULL,'Kareem','Howard','BSA','2','male'),('2024-0084',NULL,'Chiara','Bridges','BSEM','4','female'),('2024-0088',NULL,'Kadie','Key','BSBA-MM','','female'),('2024-0089',NULL,'Meredith','Murphy','BSCpE','3','female'),('2024-0099',NULL,'Laura','Eaton','BSIT','3','female'),('2024-0100',NULL,'Pauline','Dillon','BAELS','3','male'),('2024-0103',NULL,'Neve','Boyd','BSStat','4','male'),('2024-0105',NULL,'Alejandro','Oconnor','BSBA-MM','','male'),('2024-0109',NULL,'Naima','Mack','BEed-Lang','','female'),('2024-0111',NULL,'Helen','Ward','BEed-Lang','1','female'),('2024-0112',NULL,'Madeleine','Hansen','BSChem','4','male'),('2024-0118',NULL,'Courtney','Chen','BSStat','4','female'),('2024-0124',NULL,'Melody','Joyce','BSN','','female'),('2024-0132',NULL,'Jamal','Patton','BTVTEd-DraftTech','3','female'),('2024-0136',NULL,'Jack','Richards','BTLEd-HE','2','male'),('2024-0144',NULL,'Ned','Pacheco','BSMarineBio','4','female'),('2024-0146',NULL,'Dylan','Wilkerson','BSCpE','3','female'),('2024-0147',NULL,'Judith','Wiggins','BSEcon','','male'),('2024-0149',NULL,'Bobby','Lloyd','BSCerE','3','male'),('2024-0152',NULL,'Dora','Lucero','BSBA-Econ','','female'),('2024-0153',NULL,'Bella','Houston','BASocio','4','male'),('2024-0154',NULL,'Haydn','Sparks','BSME','1','female'),('2024-0158',NULL,'Ilyas','Fitzgerald','BASocio','1','female'),('2024-0166',NULL,'Danielle','Kelley','BSStat','','male'),('2024-0169',NULL,'Sylvie','Griffin','BSA','3','male'),('2024-0176',NULL,'Blake','Christensen','BASocio','3','male'),('2024-0177',NULL,'Joseph','OQuinn','BSA','3','female'),('2024-0179',NULL,'Dominik','Orozco','BSEd-Bio','4','male'),('2024-0184',NULL,'Lacie','Kelly','BSBA-MM','','female'),('2024-0186',NULL,'Chris','Tate','BSPhil','4','female'),('2024-0190',NULL,'Michelle','Rosario','BTVTEd-DraftTech','1','male'),('2024-0195',NULL,'Cleo','Saunders','BSMarineBio','3','female'),('2024-0209',NULL,'Danyal','Guerra','BSCE','2','male'),('2024-0210',NULL,'Solomon','Vaughan','BSChem','4','female'),('2024-0216',NULL,'Rohan','Odling','BTVTEd-DraftTech','1','male'),('2024-0226',NULL,'Olivier','Lindsey','BTVTEd-DraftTech','3','male'),('2024-0228',NULL,'Trystan','Lopez','BTVTEd-DraftTech','4','female');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-28 14:14:30
