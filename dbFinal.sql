-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: webp2ms
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_chat`
--

DROP TABLE IF EXISTS `app_chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(255) NOT NULL,
  `is_opened` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `timetable_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `App_chat_timetable_id_0bd368cf_fk_App_timetable_id` (`timetable_id`),
  KEY `App_chat_user_id_2ad24d87_fk_Auth_myuser_id` (`user_id`),
  CONSTRAINT `App_chat_timetable_id_0bd368cf_fk_App_timetable_id` FOREIGN KEY (`timetable_id`) REFERENCES `app_timetable` (`id`),
  CONSTRAINT `App_chat_user_id_2ad24d87_fk_Auth_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `auth_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_chat`
--

LOCK TABLES `app_chat` WRITE;
/*!40000 ALTER TABLE `app_chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_classroom`
--

DROP TABLE IF EXISTS `app_classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_classroom` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slug` varchar(200) NOT NULL,
  `capacity` int NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `desc` longtext,
  PRIMARY KEY (`id`),
  KEY `App_classroom_created_by_id_d27db5d9_fk_Auth_myuser_id` (`created_by_id`),
  CONSTRAINT `App_classroom_created_by_id_d27db5d9_fk_Auth_myuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_classroom`
--

LOCK TABLES `app_classroom` WRITE;
/*!40000 ALTER TABLE `app_classroom` DISABLE KEYS */;
INSERT INTO `app_classroom` VALUES (1,'IRAN 2',400,'2023-06-29 15:41:35.953767','2023-06-29 15:41:35.954760',1,'C\'est la salle au deuxieme etage de l\'amphi IRAN'),(2,'Padtice',300,'2023-06-29 15:42:15.932659','2023-06-29 15:42:15.932659',1,'C\'est la salle a l\'etage 0 de l\'amphi IRAN');
/*!40000 ALTER TABLE `app_classroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_notification`
--

DROP TABLE IF EXISTS `app_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `is_opened` tinyint(1) NOT NULL,
  `category` varchar(50) NOT NULL,
  `elt` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `App_notification_user_id_5ab22c9b_fk_Auth_myuser_id` (`user_id`),
  CONSTRAINT `App_notification_user_id_5ab22c9b_fk_Auth_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `auth_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_notification`
--

LOCK TABLES `app_notification` WRITE;
/*!40000 ALTER TABLE `app_notification` DISABLE KEYS */;
INSERT INTO `app_notification` VALUES (1,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 15:59:43.585423',2,0,'shedule',1),(2,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 15:59:50.586632',2,0,'shedule',2),(3,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 15:59:54.935026',2,0,'shedule',3),(4,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:23.017117',2,0,'shedule',4),(5,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:27.214352',2,0,'shedule',5),(6,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:31.625964',2,0,'shedule',6),(7,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:42.945022',2,0,'shedule',7),(8,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:51.482753',2,0,'shedule',8),(9,'Vous êtes programmé pour le 2023-06-30 en Licence 1 SEIoT','2023-06-29 16:00:58.122359',2,0,'shedule',9);
/*!40000 ALTER TABLE `app_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_subject`
--

DROP TABLE IF EXISTS `app_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_subject` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slug` varchar(200) NOT NULL,
  `code` varchar(200) DEFAULT NULL,
  `total_time` int NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `level_id` bigint DEFAULT NULL,
  `desc` longtext,
  `bgColor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `App_subject_created_by_id_28edb594_fk_Auth_myuser_id` (`created_by_id`),
  KEY `App_subject_level_id_b52e7723_fk_Auth_level_id` (`level_id`),
  CONSTRAINT `App_subject_created_by_id_28edb594_fk_Auth_myuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_myuser` (`id`),
  CONSTRAINT `App_subject_level_id_b52e7723_fk_Auth_level_id` FOREIGN KEY (`level_id`) REFERENCES `auth_level` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_subject`
--

LOCK TABLES `app_subject` WRITE;
/*!40000 ALTER TABLE `app_subject` DISABLE KEYS */;
INSERT INTO `app_subject` VALUES (1,'Anglais','348269',30,'2023-06-29 15:57:08.620884','2023-06-29 15:57:08.623721',1,1,'Cours de l','#610f0f'),(2,'Algorithmique','12HHHH',20,'2023-06-29 15:57:56.656848','2023-06-29 15:57:56.656848',1,1,'C\'est This is my portfolio to illustrate all my skills','#2bbf49');
/*!40000 ALTER TABLE `app_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_timetable`
--

DROP TABLE IF EXISTS `app_timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_timetable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` time(6) DEFAULT NULL,
  `end_time` time(6) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `classroom_id` bigint DEFAULT NULL,
  `subject_id` bigint DEFAULT NULL,
  `teacher_id` bigint DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `App_timetable_classroom_id_1d069fd0_fk_App_classroom_id` (`classroom_id`),
  KEY `App_timetable_subject_id_2d1b393f_fk_App_subject_id` (`subject_id`),
  KEY `App_timetable_teacher_id_ecf27e49_fk_Auth_myuser_id` (`teacher_id`),
  CONSTRAINT `App_timetable_classroom_id_1d069fd0_fk_App_classroom_id` FOREIGN KEY (`classroom_id`) REFERENCES `app_classroom` (`id`),
  CONSTRAINT `App_timetable_subject_id_2d1b393f_fk_App_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `app_subject` (`id`),
  CONSTRAINT `App_timetable_teacher_id_ecf27e49_fk_Auth_myuser_id` FOREIGN KEY (`teacher_id`) REFERENCES `auth_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_timetable`
--

LOCK TABLES `app_timetable` WRITE;
/*!40000 ALTER TABLE `app_timetable` DISABLE KEYS */;
INSERT INTO `app_timetable` VALUES (1,'07:00:00.000000','11:00:00.000000','2023-06-29 15:59:43.570056','2023-06-29 15:59:43.570056',1,2,2,'2023-06-30','2023-06-30'),(2,'07:00:00.000000','11:00:00.000000','2023-06-29 15:59:50.554828','2023-06-29 15:59:50.554828',1,2,2,'2023-06-30','2023-06-30'),(3,'07:00:00.000000','11:00:00.000000','2023-06-29 15:59:54.903189','2023-06-29 15:59:54.903189',1,2,2,'2023-06-30','2023-06-30'),(4,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:22.973540','2023-06-29 16:00:22.973540',1,2,2,'2023-06-30','2023-06-30'),(5,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:27.169883','2023-06-29 16:00:27.169883',1,2,2,'2023-06-30','2023-06-30'),(6,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:31.598974','2023-06-29 16:00:31.598974',1,2,2,'2023-06-30','2023-06-30'),(7,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:42.913392','2023-06-29 16:00:42.913392',1,2,2,'2023-06-30','2023-06-30'),(8,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:51.446108','2023-06-29 16:00:51.446108',2,2,2,'2023-06-30','2023-06-30'),(9,'07:00:00.000000','11:00:00.000000','2023-06-29 16:00:58.105392','2023-06-29 16:00:58.105392',2,1,2,'2023-06-30','2023-06-30');
/*!40000 ALTER TABLE `app_timetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_level`
--

DROP TABLE IF EXISTS `auth_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_level` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `total_students` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_level`
--

LOCK TABLES `auth_level` WRITE;
/*!40000 ALTER TABLE `auth_level` DISABLE KEYS */;
INSERT INTO `auth_level` VALUES (1,'Licence 1 SEIoT','2023-06-29 15:40:14.658017','2023-06-29 15:40:14.658017',200),(2,'Licence 1 SI','2023-06-29 15:40:33.380492','2023-06-29 15:40:33.380492',200),(3,'Licence 1 IA','2023-06-29 15:40:50.310457','2023-06-29 15:40:50.310457',30);
/*!40000 ALTER TABLE `auth_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_myuser`
--

DROP TABLE IF EXISTS `auth_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_myuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `reset_token` varchar(255) DEFAULT NULL,
  `reset_token_expiration` datetime(6) DEFAULT NULL,
  `is_teacher` tinyint(1) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `is_two_factor` tinyint(1) NOT NULL,
  `two_factor_code` varchar(255) DEFAULT NULL,
  `phone_num` varchar(50) DEFAULT NULL,
  `level_id` bigint DEFAULT NULL,
  `is_online` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `Auth_myuser_created_by_id_e67c44b9_fk_Auth_myuser_id` (`created_by_id`),
  KEY `Auth_myuser_level_id_9e940f34_fk_Auth_level_id` (`level_id`),
  CONSTRAINT `Auth_myuser_created_by_id_e67c44b9_fk_Auth_myuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_myuser` (`id`),
  CONSTRAINT `Auth_myuser_level_id_9e940f34_fk_Auth_level_id` FOREIGN KEY (`level_id`) REFERENCES `auth_level` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_myuser`
--

LOCK TABLES `auth_myuser` WRITE;
/*!40000 ALTER TABLE `auth_myuser` DISABLE KEYS */;
INSERT INTO `auth_myuser` VALUES (1,'pbkdf2_sha256$600000$KvEmoqqUJWYtnCAulpwBcI$EIl6cGWYQuicbEPCJLDn3m5/3Kj/6kgHvIn+f1eyQYA=','2023-06-29 15:39:10.794803','kabirou2001@gmail.com',1,1,1,'ALASSANE','Kabirou',NULL,NULL,NULL,0,'',0,NULL,NULL,NULL,1),(2,'',NULL,'kabirou2001@outlook.com',0,1,0,'HASSANE','ALASSANE',1,'MI8Fh9eXiK3K4afxf5WNUij-5JnoZeDbh0RGGNdaIO4','2023-06-29 17:55:34.237153',1,'',0,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `auth_myuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_myuser_groups`
--

DROP TABLE IF EXISTS `auth_myuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_myuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Auth_myuser_groups_myuser_id_group_id_1394ab36_uniq` (`myuser_id`,`group_id`),
  KEY `Auth_myuser_groups_group_id_1ec524e5_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Auth_myuser_groups_group_id_1ec524e5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `Auth_myuser_groups_myuser_id_9ce6a72e_fk_Auth_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `auth_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_myuser_groups`
--

LOCK TABLES `auth_myuser_groups` WRITE;
/*!40000 ALTER TABLE `auth_myuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_myuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_myuser_user_permissions`
--

DROP TABLE IF EXISTS `auth_myuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_myuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `myuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Auth_myuser_user_permiss_myuser_id_permission_id_bd9d61fa_uniq` (`myuser_id`,`permission_id`),
  KEY `Auth_myuser_user_per_permission_id_7f03e8c0_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Auth_myuser_user_per_myuser_id_a3534e4a_fk_Auth_myus` FOREIGN KEY (`myuser_id`) REFERENCES `auth_myuser` (`id`),
  CONSTRAINT `Auth_myuser_user_per_permission_id_7f03e8c0_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_myuser_user_permissions`
--

LOCK TABLES `auth_myuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_myuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_myuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add my user',6,'add_myuser'),(22,'Can change my user',6,'change_myuser'),(23,'Can delete my user',6,'delete_myuser'),(24,'Can view my user',6,'view_myuser'),(25,'Can add level',7,'add_level'),(26,'Can change level',7,'change_level'),(27,'Can delete level',7,'delete_level'),(28,'Can view level',7,'view_level'),(29,'Can add classroom',8,'add_classroom'),(30,'Can change classroom',8,'change_classroom'),(31,'Can delete classroom',8,'delete_classroom'),(32,'Can view classroom',8,'view_classroom'),(33,'Can add subject',9,'add_subject'),(34,'Can change subject',9,'change_subject'),(35,'Can delete subject',9,'delete_subject'),(36,'Can view subject',9,'view_subject'),(37,'Can add timetable',10,'add_timetable'),(38,'Can change timetable',10,'change_timetable'),(39,'Can delete timetable',10,'delete_timetable'),(40,'Can view timetable',10,'view_timetable'),(41,'Can add notification',11,'add_notification'),(42,'Can change notification',11,'change_notification'),(43,'Can delete notification',11,'delete_notification'),(44,'Can view notification',11,'view_notification'),(45,'Can add chat',12,'add_chat'),(46,'Can change chat',12,'change_chat'),(47,'Can delete chat',12,'delete_chat'),(48,'Can view chat',12,'view_chat');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Auth_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Auth_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `auth_myuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(12,'App','chat'),(8,'App','classroom'),(11,'App','notification'),(9,'App','subject'),(10,'App','timetable'),(3,'auth','group'),(7,'Auth','level'),(6,'Auth','myuser'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Auth','0001_initial','2023-06-29 15:26:41.465666'),(2,'contenttypes','0001_initial','2023-06-29 15:26:41.619337'),(3,'contenttypes','0002_remove_content_type_name','2023-06-29 15:26:41.784266'),(4,'auth','0001_initial','2023-06-29 15:26:42.527858'),(5,'auth','0002_alter_permission_name_max_length','2023-06-29 15:26:42.721971'),(6,'auth','0003_alter_user_email_max_length','2023-06-29 15:26:42.739018'),(7,'auth','0004_alter_user_username_opts','2023-06-29 15:26:42.754144'),(8,'auth','0005_alter_user_last_login_null','2023-06-29 15:26:42.771533'),(9,'auth','0006_require_contenttypes_0002','2023-06-29 15:26:42.780994'),(10,'auth','0007_alter_validators_add_error_messages','2023-06-29 15:26:42.804273'),(11,'auth','0008_alter_user_username_max_length','2023-06-29 15:26:42.820797'),(12,'auth','0009_alter_user_last_name_max_length','2023-06-29 15:26:42.843400'),(13,'auth','0010_alter_group_name_max_length','2023-06-29 15:26:42.903010'),(14,'auth','0011_update_proxy_permissions','2023-06-29 15:26:42.928645'),(15,'auth','0012_alter_user_first_name_max_length','2023-06-29 15:26:42.947764'),(16,'Auth','0002_myuser_groups_myuser_is_superuser_and_more','2023-06-29 15:26:43.530134'),(17,'Auth','0003_myuser_is_active_myuser_is_staff','2023-06-29 15:26:43.755706'),(18,'Auth','0004_myuser_first_name_myuser_last_name','2023-06-29 15:26:43.982498'),(19,'Auth','0005_myuser_created_by_myuser_reset_token_and_more','2023-06-29 15:26:44.309756'),(20,'Auth','0006_myuser_is_teacher','2023-06-29 15:26:44.511295'),(21,'Auth','0007_myuser_avatar','2023-06-29 15:26:44.658860'),(22,'Auth','0008_alter_myuser_is_teacher','2023-06-29 15:26:44.693222'),(23,'Auth','0009_myuser_is_two_factor_myuser_two_factor_code','2023-06-29 15:26:44.915733'),(24,'Auth','0010_level_myuser_phone_num_myuser_level','2023-06-29 15:26:45.184740'),(25,'App','0001_initial','2023-06-29 15:26:46.018802'),(26,'App','0002_auto_20230617_1509','2023-06-29 15:26:46.095886'),(27,'App','0003_subjects_created_at_subjects_created_by_and_more','2023-06-29 15:26:46.483967'),(28,'App','0004_classroom_subject_timetable_remove_levels_created_by_and_more','2023-06-29 15:26:48.985822'),(29,'App','0005_classroom_desc_subject_desc','2023-06-29 15:26:49.214481'),(30,'App','0006_remove_timetable_week','2023-06-29 15:26:49.336248'),(31,'App','0007_timetable_end_date_timetable_start_date_and_more','2023-06-29 15:26:49.712566'),(32,'App','0008_rename_teach_by_timetable_teacher','2023-06-29 15:26:50.013253'),(33,'App','0009_remove_timetable_level','2023-06-29 15:26:50.230258'),(34,'App','0010_subject_bgcolor','2023-06-29 15:26:50.315659'),(35,'App','0011_alter_subject_bgcolor','2023-06-29 15:26:50.459147'),(36,'App','0012_notification','2023-06-29 15:26:50.613009'),(37,'App','0013_notification_is_opened','2023-06-29 15:26:50.684295'),(38,'App','0014_alter_notification_is_opened','2023-06-29 15:26:50.711768'),(39,'App','0015_chat','2023-06-29 15:26:50.879367'),(40,'App','0016_chat_created_by','2023-06-29 15:26:51.030810'),(41,'App','0017_rename_created_by_chat_user','2023-06-29 15:26:51.230958'),(42,'App','0018_alter_chat_options_notification_category','2023-06-29 15:26:51.340664'),(43,'App','0019_notification_elt','2023-06-29 15:26:51.418054'),(44,'Auth','0011_level_total_students','2023-06-29 15:26:51.520751'),(45,'Auth','0012_alter_myuser_level','2023-06-29 15:26:51.552854'),(46,'Auth','0013_myuser_is_online','2023-06-29 15:26:51.780880'),(47,'admin','0001_initial','2023-06-29 15:26:52.157590'),(48,'admin','0002_logentry_remove_auto_add','2023-06-29 15:26:52.193773'),(49,'admin','0003_logentry_add_action_flag_choices','2023-06-29 15:26:52.249815'),(50,'sessions','0001_initial','2023-06-29 15:26:52.352367');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('h0c1zf2rbaww41xjrjm70sic865db09h','.eJxVjMsOwiAURP-FtSFAebp07zeQS-9FqgaS0q6M_64kXehy5pyZF4uwbyXunda4IDszyU6_XYL5QXUAvEO9NT63uq1L4kPhB-382pCel8P9OyjQy1hnkoSGpqCVmrXzDrP9JgQbhCcvVFYOjaAkvRUKtUnJ02QyZC-zCOz9AfHvOBg:1qEtji:v08byawmqm2VwHDo12fUtqivczTi7kzNPTgF8eOt3zM','2023-07-13 15:39:10.798839');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-29 17:03:14
