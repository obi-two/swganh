-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.1.63-community - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL version:             7.0.0.4053
-- Date/time:                    2012-10-14 17:58:59
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;

-- Dumping structure for table galaxy.name_fictionally_reserved
DROP TABLE IF EXISTS `name_fictionally_reserved`;
CREATE TABLE IF NOT EXISTS `name_fictionally_reserved` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- Dumping data for table galaxy.name_fictionally_reserved: ~9 rows (approximately)
/*!40000 ALTER TABLE `name_fictionally_reserved` DISABLE KEYS */;
INSERT INTO `name_fictionally_reserved` (`id`, `name`) VALUES
	(1, 'luke'),
	(2, 'darth'),
	(3, 'vader'),
	(4, 'leia'),
	(5, 'chewbacca'),
	(6, 'yoda'),
	(7, 'emperor'),
	(8, 'stormtrooper'),
	(9, 'tk');
/*!40000 ALTER TABLE `name_fictionally_reserved` ENABLE KEYS */;
/*!40014 SET FOREIGN_KEY_CHECKS=1 */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
