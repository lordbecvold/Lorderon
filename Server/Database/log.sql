-- MySQL dump 10.13  Distrib 5.6.50, for FreeBSD12.1 (amd64)
--
-- Host: localhost    Database: log
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
-- Table structure for table `GameTimeLog`
--

DROP TABLE IF EXISTS `GameTimeLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GameTimeLog` (
  `login` varbinary(16) DEFAULT NULL,
  `type` int(11) unsigned DEFAULT NULL,
  `logon_time` datetime DEFAULT NULL,
  `logout_time` datetime DEFAULT NULL,
  `use_time` int(15) unsigned DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL,
  `server` varbinary(56) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GameTimeLog`
--

LOCK TABLES `GameTimeLog` WRITE;
/*!40000 ALTER TABLE `GameTimeLog` DISABLE KEYS */;
/*!40000 ALTER TABLE `GameTimeLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bootlog`
--

DROP TABLE IF EXISTS `bootlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bootlog` (
  `time` datetime DEFAULT NULL,
  `hostname` varbinary(56) DEFAULT NULL,
  `channel` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bootlog`
--

LOCK TABLES `bootlog` WRITE;
/*!40000 ALTER TABLE `bootlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `bootlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `change_empire`
--

DROP TABLE IF EXISTS `change_empire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `change_empire` (
  `account_id` int(11) unsigned NOT NULL DEFAULT '0',
  `change_count` int(11) DEFAULT NULL,
  `data` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `change_empire`
--

LOCK TABLES `change_empire` WRITE;
/*!40000 ALTER TABLE `change_empire` DISABLE KEYS */;
/*!40000 ALTER TABLE `change_empire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `change_name`
--

DROP TABLE IF EXISTS `change_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `change_name` (
  `pid` int(11) unsigned DEFAULT NULL,
  `old_name` varbinary(16) DEFAULT NULL,
  `new_name` varbinary(16) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `change_name`
--

LOCK TABLES `change_name` WRITE;
/*!40000 ALTER TABLE `change_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `change_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_log`
--

DROP TABLE IF EXISTS `chat_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_log` (
  `where` int(10) unsigned NOT NULL,
  `who_id` int(10) unsigned NOT NULL,
  `who_name` varchar(25) NOT NULL,
  `whom_id` int(10) unsigned DEFAULT NULL,
  `whom_name` varchar(25) DEFAULT NULL,
  `type` enum('NORMAL','WHISPER','PARTY','GUILD') NOT NULL,
  `msg` varbinary(512) NOT NULL,
  `when` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ip` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_log`
--

LOCK TABLES `chat_log` WRITE;
/*!40000 ALTER TABLE `chat_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `command_log`
--

DROP TABLE IF EXISTS `command_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `command_log` (
  `userid` int(11) unsigned DEFAULT NULL,
  `server` int(11) DEFAULT '999',
  `ip` varbinary(15) DEFAULT NULL,
  `port` int(11) unsigned DEFAULT NULL,
  `username` varbinary(16) DEFAULT NULL,
  `command` varbinary(300) DEFAULT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `command_log`
--

LOCK TABLES `command_log` WRITE;
/*!40000 ALTER TABLE `command_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `command_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cube`
--

DROP TABLE IF EXISTS `cube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cube` (
  `pid` int(11) unsigned DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `x` int(11) unsigned DEFAULT NULL,
  `y` int(11) unsigned DEFAULT NULL,
  `item_vnum` int(11) unsigned DEFAULT NULL,
  `item_uid` int(11) unsigned DEFAULT NULL,
  `item_count` int(11) DEFAULT NULL,
  `success` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cube`
--

LOCK TABLES `cube` WRITE;
/*!40000 ALTER TABLE `cube` DISABLE KEYS */;
/*!40000 ALTER TABLE `cube` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dragon_slay_log`
--

DROP TABLE IF EXISTS `dragon_slay_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dragon_slay_log` (
  `guild_id` int(11) unsigned NOT NULL,
  `vnum` int(11) unsigned NOT NULL,
  `start_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dragon_slay_log`
--

LOCK TABLES `dragon_slay_log` WRITE;
/*!40000 ALTER TABLE `dragon_slay_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `dragon_slay_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_log`
--

DROP TABLE IF EXISTS `fish_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fish_log` (
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `player_id` int(10) unsigned NOT NULL DEFAULT '0',
  `map_index` tinyint(4) NOT NULL DEFAULT '0',
  `fish_id` int(10) unsigned NOT NULL DEFAULT '0',
  `fishing_level` int(11) NOT NULL DEFAULT '0',
  `waiting_time` int(11) NOT NULL DEFAULT '0',
  `success` tinyint(4) NOT NULL DEFAULT '0',
  `size` smallint(6) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_log`
--

LOCK TABLES `fish_log` WRITE;
/*!40000 ALTER TABLE `fish_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `fish_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goldlog`
--

DROP TABLE IF EXISTS `goldlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goldlog` (
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `what` int(11) unsigned DEFAULT NULL,
  `how` varbinary(33) DEFAULT NULL COMMENT 'contains: QUEST, BUY, SELL, SHOP_BUY, SHOP_SELL, EXCHANGE_TAKE, EXCHANGE_GIVE',
  `hint` varbinary(80) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goldlog`
--

LOCK TABLES `goldlog` WRITE;
/*!40000 ALTER TABLE `goldlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `goldlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hack_crc_log`
--

DROP TABLE IF EXISTS `hack_crc_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hack_crc_log` (
  `time` datetime DEFAULT NULL,
  `login` varbinary(16) DEFAULT NULL,
  `name` varbinary(16) DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL,
  `server` varbinary(56) DEFAULT NULL,
  `why` varbinary(33) DEFAULT NULL,
  `crc` int(11) unsigned DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hack_crc_log`
--

LOCK TABLES `hack_crc_log` WRITE;
/*!40000 ALTER TABLE `hack_crc_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `hack_crc_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hack_log`
--

DROP TABLE IF EXISTS `hack_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hack_log` (
  `time` datetime DEFAULT NULL,
  `login` varbinary(16) DEFAULT NULL,
  `name` varbinary(16) DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL,
  `server` varbinary(56) DEFAULT NULL,
  `why` varbinary(33) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hack_log`
--

LOCK TABLES `hack_log` WRITE;
/*!40000 ALTER TABLE `hack_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `hack_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackshield_log`
--

DROP TABLE IF EXISTS `hackshield_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hackshield_log` (
  `time` datetime DEFAULT NULL,
  `account_id` int(11) unsigned DEFAULT NULL,
  `login` varbinary(16) DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `name` varbinary(16) DEFAULT NULL,
  `reason` int(11) unsigned DEFAULT NULL,
  `ip` int(11) unsigned DEFAULT NULL COMMENT 'inet_aton(''%s'')'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackshield_log`
--

LOCK TABLES `hackshield_log` WRITE;
/*!40000 ALTER TABLE `hackshield_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `hackshield_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invalid_server_log`
--

DROP TABLE IF EXISTS `invalid_server_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invalid_server_log` (
  `locale_type` int(11) unsigned DEFAULT NULL,
  `log_date` datetime DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL,
  `revision` varbinary(16) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invalid_server_log`
--

LOCK TABLES `invalid_server_log` WRITE;
/*!40000 ALTER TABLE `invalid_server_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `invalid_server_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levellog`
--

DROP TABLE IF EXISTS `levellog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `levellog` (
  `name` varbinary(16) DEFAULT NULL,
  `level` int(11) unsigned DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `account_id` int(11) unsigned DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL COMMENT 'contains REPLACE query!',
  `playtime` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levellog`
--

LOCK TABLES `levellog` WRITE;
/*!40000 ALTER TABLE `levellog` DISABLE KEYS */;
INSERT INTO `levellog` VALUES ('[COMA]Ivus',120,'2020-05-27 16:25:38',1,2,1),('[TGM]LowLike',120,'2020-05-27 16:29:26',1,3,0),('[EM]SoulStone',120,'2020-05-27 16:33:06',1,4,0),('[Owner]Lordbecvo',120,'2020-05-27 16:36:31',1,1,1);
/*!40000 ALTER TABLE `levellog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `type` varbinary(20) DEFAULT NULL COMMENT 'contains: CHARACTER, ITEM',
  `time` datetime DEFAULT NULL,
  `who` int(11) unsigned DEFAULT NULL,
  `x` int(11) unsigned DEFAULT NULL,
  `y` int(11) unsigned DEFAULT NULL,
  `what` bigint(11) unsigned DEFAULT NULL,
  `how` varbinary(50) DEFAULT NULL,
  `hint` varbinary(80) DEFAULT NULL COMMENT 'snprintf with 80u size',
  `ip` varbinary(15) DEFAULT NULL,
  `vnum` int(11) unsigned DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginlog`
--

DROP TABLE IF EXISTS `loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loginlog` (
  `type` varbinary(20) DEFAULT NULL COMMENT 'contains: LOGIN, LOGOUT',
  `time` datetime DEFAULT NULL,
  `channel` int(11) DEFAULT NULL,
  `account_id` int(11) unsigned DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `job` int(11) DEFAULT NULL,
  `playtime` int(11) unsigned DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginlog`
--

LOCK TABLES `loginlog` WRITE;
/*!40000 ALTER TABLE `loginlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `loginlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginlog2`
--

DROP TABLE IF EXISTS `loginlog2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loginlog2` (
  `type` varbinary(20) DEFAULT NULL COMMENT 'contains: VALID, INVALID',
  `is_gm` varbinary(20) DEFAULT NULL COMMENT 'contains: Y, N',
  `login_time` datetime DEFAULT NULL,
  `channel` int(11) DEFAULT NULL,
  `account_id` int(11) unsigned DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `ip` int(11) unsigned DEFAULT NULL COMMENT 'inet_aton(''%s'')',
  `client_version` varbinary(11) DEFAULT NULL COMMENT 'maybe 1215955205',
  `logout_time` datetime DEFAULT NULL,
  `playtime` datetime DEFAULT NULL,
  `id` int(11) DEFAULT NULL COMMENT 'maybe primary'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginlog2`
--

LOCK TABLES `loginlog2` WRITE;
/*!40000 ALTER TABLE `loginlog2` DISABLE KEYS */;
/*!40000 ALTER TABLE `loginlog2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `money_log`
--

DROP TABLE IF EXISTS `money_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `money_log` (
  `time` datetime DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `vnum` int(11) DEFAULT NULL,
  `gold` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `money_log`
--

LOCK TABLES `money_log` WRITE;
/*!40000 ALTER TABLE `money_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `money_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pcbang_loginlog`
--

DROP TABLE IF EXISTS `pcbang_loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pcbang_loginlog` (
  `time` datetime DEFAULT NULL,
  `pcbang_id` int(11) unsigned DEFAULT NULL,
  `ip` varbinary(15) DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `play_time` int(11) unsigned DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pcbang_loginlog`
--

LOCK TABLES `pcbang_loginlog` WRITE;
/*!40000 ALTER TABLE `pcbang_loginlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `pcbang_loginlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quest_reward_log`
--

DROP TABLE IF EXISTS `quest_reward_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quest_reward_log` (
  `quest_name` varbinary(56) DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT NULL,
  `level` int(11) unsigned DEFAULT NULL,
  `type` int(11) DEFAULT NULL COMMENT 'contains: EXP, ITEM',
  `how` int(11) unsigned DEFAULT NULL,
  `hint` int(11) unsigned DEFAULT NULL,
  `when` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quest_reward_log`
--

LOCK TABLES `quest_reward_log` WRITE;
/*!40000 ALTER TABLE `quest_reward_log` DISABLE KEYS */;
INSERT INTO `quest_reward_log` VALUES ('give_basic_weapon',1,1,2,19,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,12209,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,11209,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,3009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,30201,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,72726,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,72730,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,70007,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,71164,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,53006,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,70038,250,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,15009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,13009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,14009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,16009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,17009,1,'2020-05-27 16:06:45'),('give_basic_weapon',1,1,2,18009,1,'2020-05-27 16:06:45'),('give_basic_weapon',2,1,2,1009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,12349,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,11409,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,2009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,8005,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,19,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,30201,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,72726,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,72730,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,70007,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,71164,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,53006,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,70038,250,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,15009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,13009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,14009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,16009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,17009,1,'2020-05-27 16:09:49'),('give_basic_weapon',2,1,2,18009,1,'2020-05-27 16:09:49'),('give_basic_weapon',3,1,2,19,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,12489,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,11609,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,30201,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,72726,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,72730,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,70007,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,71164,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,53006,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,70038,250,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,15009,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,13009,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,14009,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,16009,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,17009,1,'2020-05-27 16:10:42'),('give_basic_weapon',3,1,2,18009,1,'2020-05-27 16:10:42'),('give_basic_weapon',4,1,2,7009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,12629,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,11809,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,30201,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,72726,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,72730,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,70007,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,71164,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,53006,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,70038,250,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,15009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,13009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,14009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,16009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,17009,1,'2020-05-27 16:11:36'),('give_basic_weapon',4,1,2,18009,1,'2020-05-27 16:11:36');
/*!40000 ALTER TABLE `quest_reward_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refinelog`
--

DROP TABLE IF EXISTS `refinelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `refinelog` (
  `pid` int(11) unsigned DEFAULT NULL,
  `item_name` varbinary(56) DEFAULT NULL,
  `item_id` int(11) unsigned DEFAULT NULL,
  `step` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `is_success` tinyint(1) DEFAULT NULL,
  `setType` varchar(20) DEFAULT NULL COMMENT 'contains: HYUNIRON, POWER, SCROLL'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refinelog`
--

LOCK TABLES `refinelog` WRITE;
/*!40000 ALTER TABLE `refinelog` DISABLE KEYS */;
/*!40000 ALTER TABLE `refinelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shout_log`
--

DROP TABLE IF EXISTS `shout_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shout_log` (
  `when` datetime DEFAULT NULL,
  `where` int(11) DEFAULT NULL,
  `empire` int(11) DEFAULT NULL,
  `message` varbinary(512) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shout_log`
--

LOCK TABLES `shout_log` WRITE;
/*!40000 ALTER TABLE `shout_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `shout_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speed_hack`
--

DROP TABLE IF EXISTS `speed_hack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `speed_hack` (
  `pid` int(11) unsigned DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `x` int(11) DEFAULT NULL,
  `y` int(11) DEFAULT NULL,
  `hack_count` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speed_hack`
--

LOCK TABLES `speed_hack` WRITE;
/*!40000 ALTER TABLE `speed_hack` DISABLE KEYS */;
/*!40000 ALTER TABLE `speed_hack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vcard_log`
--

DROP TABLE IF EXISTS `vcard_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vcard_log` (
  `vcard_id` int(11) unsigned DEFAULT NULL,
  `x` int(11) unsigned DEFAULT NULL,
  `y` int(11) unsigned DEFAULT NULL,
  `hostname` varbinary(56) DEFAULT NULL,
  `giver_name` varbinary(16) DEFAULT NULL,
  `giver_ip` varbinary(15) DEFAULT NULL,
  `taker_name` varbinary(16) DEFAULT NULL,
  `taker_ip` varbinary(15) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vcard_log`
--

LOCK TABLES `vcard_log` WRITE;
/*!40000 ALTER TABLE `vcard_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `vcard_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-28 19:25:03
