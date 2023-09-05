-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: protect_these_users
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(145) NOT NULL,
  `last_name` varchar(145) NOT NULL,
  `email` varchar(145) NOT NULL,
  `password` varchar(145) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Probando','Probando','Probando@gmail.com','Probando123','2023-08-22 21:14:44','2023-08-22 21:14:44'),(2,'Enrique','Torales','enri@gmail.com','123456enri','2023-08-22 22:18:45','2023-08-22 22:18:45'),(3,'Apolo','Weber','cw016@hotmail.com','josejose','2023-08-22 23:47:24','2023-08-22 23:47:24'),(4,'Rober','Esqueche','esteban_87@gmail.com','121212','2023-08-22 23:59:50','2023-08-22 23:59:50'),(5,'Del Carmen','Morinigo','morinigo_del_carmen@hotmail.com','$2b$12$G.df/owWaUX8H8e.6BAS9.PQgomD2tVaURYlTQaPvNj1Vp4FjyVz2','2023-08-23 13:31:25','2023-08-23 13:31:25'),(6,'Francisca','Roman','roman_francisca@gmail.com','$2b$12$UlWlh82e4OUu2Q3QwbSkkueNtaawYW0qLXdgP.9IKlbPaJb0XptkS','2023-08-23 13:33:27','2023-08-23 13:33:27'),(7,'Rober','todos','estamos_todos@hotmail.com','$2b$12$KnfnYZBbT8qQ/DVBcmwPuOjWzy0CHOtLNnwfMRUpRTzRChdDhNJ7y','2023-08-23 13:37:38','2023-08-23 13:37:38'),(8,'Rober','fjoaj','probando.prob1ando@gmail.com','$2b$12$uFgTRYtlIGXewunAzat..eiB6B3ZCGm.9SZWS1CWu6YhkxW2NsySm','2023-08-23 13:39:19','2023-08-23 13:39:19'),(9,'alba','ñil','albanhil@hotmail.com','$2b$12$u6JY8KEqcrOfmQSHwNGmuOfDZk4K8Css4dWSBxvveqch4RbvHW60C','2023-08-23 13:56:22','2023-08-23 13:56:22'),(10,'Enrique','Torales','enri@gmail.com','123456enri','2023-08-23 14:02:59','2023-08-23 14:02:59'),(11,'Roberto','Esqueche','roberto_esqueche@hotmail.com','$2b$12$qrUiOmu2UhEmIW0aEHrEMuBwep69SEgKHmT6ckZuFI77cnk11pnB2','2023-08-23 14:04:13','2023-08-23 14:04:13');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-23 10:41:17
