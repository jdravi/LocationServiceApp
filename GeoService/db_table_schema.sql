-- Adminer 4.6.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';

DROP DATABASE IF EXISTS `LocationInfo`;
CREATE DATABASE `LocationInfo` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `LocationInfo`;

DROP TABLE IF EXISTS `CityDetails`;
CREATE TABLE `CityDetails` (
  `CityId` int(11) NOT NULL AUTO_INCREMENT,
  `CityName` varchar(255) NOT NULL,
  PRIMARY KEY (`CityId`),
  UNIQUE KEY `CityName` (`CityName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `LocalityInfo`;
CREATE TABLE `LocalityInfo` (
  `LocalityId` int(12) NOT NULL AUTO_INCREMENT,
  `LocalityName` varchar(255) NOT NULL,
  `CityId` int(11) NOT NULL,
  `Latitude` double NOT NULL,
  `Longitude` double NOT NULL,
  PRIMARY KEY (`LocalityId`),
  KEY `CityId` (`CityId`),
  CONSTRAINT `LocalityInfo_ibfk_1` FOREIGN KEY (`CityId`) REFERENCES `CityDetails` (`CityId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2018-11-24 16:54:13