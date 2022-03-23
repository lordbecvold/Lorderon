-- MySQL dump 10.13  Distrib 5.6.50, for FreeBSD12.1 (amd64)
--
-- Host: localhost    Database: common
-- ------------------------------------------------------
-- Server version	5.6.50

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exp_table`
--

DROP TABLE IF EXISTS `exp_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exp_table` (
  `level` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `exp` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`level`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exp_table`
--

LOCK TABLES `exp_table` WRITE;
/*!40000 ALTER TABLE `exp_table` DISABLE KEYS */;
INSERT INTO `exp_table` VALUES (1,150),(2,400),(3,750),(4,1250),(5,2150),(6,3600),(7,5500),(8,8500),(9,12000),(10,16500),(11,19300),(12,21500),(13,38000),(14,50000),(15,65000),(16,84500),(17,109500),(18,141500),(19,182500),(20,236000),(21,336000),(22,352500),(23,406500),(24,468500),(25,538500),(26,618500),(27,709000),(28,812000),(29,928500),(30,1061000),(31,1210500),(32,1380500),(33,1572500),(34,1790000),(35,2036500),(36,2316000),(37,2597000),(38,2858500),(39,3132000),(40,3418500),(41,3800000),(42,4137000),(43,4495000),(44,4876500),(45,5280000),(46,5705000),(47,6160000),(48,6635000),(49,7140000),(50,7670000),(51,8435000),(52,9480000),(53,9990000),(54,10710000),(55,11465000),(56,12265000),(57,13100000),(58,13980000),(59,14900000),(60,16390000),(61,18030000),(62,19835000),(63,43640000),(64,21820000),(65,26400000),(66,29040000),(67,31945000),(68,35140000),(69,38655000),(70,42520000),(71,46770000),(72,51450000),(73,56600000),(74,62250000),(75,68500000),(76,75350000),(77,82850000),(78,118495000),(79,130000000),(80,143390000),(81,157690000),(82,173485000),(83,190840000),(84,209885000),(85,230000000),(86,254020000),(87,279370000),(88,307320000),(89,338065000),(90,371865000),(91,520611000),(92,572672100),(93,632672100),(94,692933241),(95,762226565),(96,838449221),(97,922294144),(98,1014523558),(99,1025000000),(100,1075000000),(101,1105000000),(102,1125000000),(103,1140000000),(104,1155000000),(105,1165000000),(106,1175000000),(107,1185000000),(108,1185000000),(109,1200000000),(110,1200000000),(111,1210000000),(112,1210000000),(113,1220000000),(114,1220000000),(115,1230000000),(116,1230000000),(117,1240000000),(118,1240000000),(119,1245000000),(120,1245000000);
/*!40000 ALTER TABLE `exp_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gmhost`
--

DROP TABLE IF EXISTS `gmhost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gmhost` (
  `mIP` varchar(16) NOT NULL DEFAULT '',
  PRIMARY KEY (`mIP`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gmhost`
--

LOCK TABLES `gmhost` WRITE;
/*!40000 ALTER TABLE `gmhost` DISABLE KEYS */;
INSERT INTO `gmhost` VALUES ('127.0.0.1');
/*!40000 ALTER TABLE `gmhost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gmlist`
--

DROP TABLE IF EXISTS `gmlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gmlist` (
  `mID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mAccount` varchar(16) NOT NULL DEFAULT '',
  `mName` varchar(30) NOT NULL DEFAULT '',
  `mContactIP` varchar(16) NOT NULL DEFAULT '',
  `mServerIP` varchar(16) NOT NULL DEFAULT 'ALL',
  `mAuthority` enum('IMPLEMENTOR','HIGH_WIZARD','GOD','LOW_WIZARD','PLAYER') NOT NULL DEFAULT 'PLAYER',
  PRIMARY KEY (`mID`)
) ENGINE=MyISAM AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gmlist`
--

LOCK TABLES `gmlist` WRITE;
/*!40000 ALTER TABLE `gmlist` DISABLE KEYS */;
INSERT INTO `gmlist` VALUES (2,'lordbecvold','[COMA]Ivus','0','ALL','IMPLEMENTOR'),(3,'lordbecvold','[TGM]LowLike','0','ALL','IMPLEMENTOR'),(4,'lordbecvold','[EM]SoulStone','0','ALL','IMPLEMENTOR'),(1,'lordbecvold','[Owner]Lordbecvold','0','ALL','IMPLEMENTOR');
/*!40000 ALTER TABLE `gmlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locale`
--

DROP TABLE IF EXISTS `locale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locale` (
  `mKey` varchar(255) NOT NULL DEFAULT '',
  `mValue` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`mKey`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locale`
--

LOCK TABLES `locale` WRITE;
/*!40000 ALTER TABLE `locale` DISABLE KEYS */;
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE0','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE1','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE2','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE3','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE4','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE5','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE6','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('SKILL_POWER_BY_LEVEL_TYPE7','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125'),('LOCALE','czech'),('DB_NAME_COLUMN','locale_name'),('SKILL_DAMAGE_BY_LEVEL_UNDER_90','0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'),('SKILL_DAMAGE_BY_LEVEL_UNDER_45','0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'),('SKILL_POWER_BY_LEVEL','0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
/*!40000 ALTER TABLE `locale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `priv_settings`
--

DROP TABLE IF EXISTS `priv_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `priv_settings` (
  `priv_type` enum('PLAYER','GUILD','EMPIRE') NOT NULL DEFAULT 'EMPIRE' COMMENT 'GUILD and PLAYER are untested.',
  `id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'this is for empire_id, player_id or guild_id',
  `type` int(10) unsigned NOT NULL DEFAULT '4' COMMENT '1:item_drop, 2:gold_drop, 3:gold10_drop, 4:exp (1~4)',
  `value` int(11) NOT NULL DEFAULT '0' COMMENT '0~1000%',
  `duration` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`priv_type`,`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `priv_settings`
--

LOCK TABLES `priv_settings` WRITE;
/*!40000 ALTER TABLE `priv_settings` DISABLE KEYS */;
/*!40000 ALTER TABLE `priv_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spam_db`
--

DROP TABLE IF EXISTS `spam_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spam_db` (
  `word` varchar(255) NOT NULL,
  `score` int(3) NOT NULL DEFAULT '1',
  `type` enum('SPAM','MAPS') NOT NULL DEFAULT 'SPAM',
  PRIMARY KEY (`word`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spam_db`
--

LOCK TABLES `spam_db` WRITE;
/*!40000 ALTER TABLE `spam_db` DISABLE KEYS */;
/*!40000 ALTER TABLE `spam_db` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-28 19:24:31
