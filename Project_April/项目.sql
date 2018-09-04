-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: user_register
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

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
-- Table structure for table `boke`
--

DROP TABLE IF EXISTS `boke`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boke` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(80) NOT NULL,
  `conntent` text NOT NULL,
  `faburen` varchar(40) NOT NULL,
  `time1` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `com_num` int(11) NOT NULL DEFAULT '0',
  `page_view` int(11) NOT NULL DEFAULT '0',
  `userId` int(11) DEFAULT NULL,
  `isdelete` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_user` (`userId`),
  CONSTRAINT `fk_user` FOREIGN KEY (`userId`) REFERENCES `register` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boke`
--

LOCK TABLES `boke` WRITE;
/*!40000 ALTER TABLE `boke` DISABLE KEYS */;
INSERT INTO `boke` VALUES (3,'王一凡','吃屎','qq123','2018-09-03 13:25:50',4,8,2,0),(4,'激动的要理由','把我的梦都摇醒了','qq123','2018-09-03 13:03:26',2,7,2,0),(5,'测试评论','用户登录状态下评论别人的博客','ww1232','2018-09-03 13:27:52',3,3,3,1);
/*!40000 ALTER TABLE `boke` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commint`
--

DROP TABLE IF EXISTS `commint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(40) NOT NULL,
  `time2` datetime NOT NULL,
  `comment` text NOT NULL,
  `userSex` int(1) NOT NULL,
  `userID` int(11) DEFAULT NULL,
  `bokeID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`userID`),
  KEY `bokeID` (`bokeID`),
  CONSTRAINT `commint_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `register` (`user_id`),
  CONSTRAINT `commint_ibfk_2` FOREIGN KEY (`bokeID`) REFERENCES `register` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commint`
--

LOCK TABLES `commint` WRITE;
/*!40000 ALTER TABLE `commint` DISABLE KEYS */;
INSERT INTO `commint` VALUES (1,'qq123','2018-09-01 06:32:40','测试',1,2,5),(2,'王一凡','2018-09-01 06:39:17','测试2',1,5,5),(3,'qq123','2018-09-01 12:36:14','最后测试',1,2,5),(4,'ww1232','2018-09-03 11:36:50','此文一出可谓是惊天地泣鬼神,堪称文曲星下凡!',1,3,3),(5,'ww1232','2018-09-03 11:59:28','真好',1,3,4),(6,'ww1232','2018-09-03 11:59:28','哈喽',1,3,3),(7,'ww1232','2018-09-03 11:59:28','haohel',1,3,3),(8,'ww1232','2018-09-03 12:59:19','hhhhhhhhhh',1,3,4),(9,'ww1232','2018-09-03 13:01:38','hahaherw',1,3,4),(10,'ww1232','2018-09-03 13:07:56','',1,3,3);
/*!40000 ALTER TABLE `commint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `register` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_token` varchar(30) NOT NULL,
  `user_name` varchar(25) NOT NULL,
  `user_passwd` varchar(100) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `user_gender` int(1) NOT NULL DEFAULT '1',
  `user_age` int(4) DEFAULT NULL,
  `user_state` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`),
  KEY `proof2` (`user_email`),
  KEY `proof` (`user_name`,`user_passwd`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (2,'qq123579','qq123','aa123111','21323234234@qq.com',1,23,0),(3,'ww1232-906','ww1232','123123','1231232143@qq.com',1,34,0),(4,'xd123-240','xd123','a1232323','123123@qq.com',1,23,1),(5,'王一凡-48','王一凡','qa123444','123212312132@qq.com',1,31,0),(6,'正旱厕-207','正旱厕','qqaa1234','1231423423@qq.com',1,21,0),(7,'lk23-824','lk23','aa123333','2341231244@qq.com',1,20,0),(8,'cyj11-597','cyj11','cc123111','232341231@qq.com',0,20,0),(9,'lmn333-795','lmn333','aq112233','234235634@qq.com',0,17,0),(10,'zcfq21-374','zcfq21','wq123123','23412334@qq.com',1,24,0);
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-03 21:49:42
