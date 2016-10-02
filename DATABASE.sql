-- Adminer 4.2.5 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

CREATE TABLE `loc` (
  `time` bigint(14) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `latitud` decimal(13,10) NOT NULL,
  `longitud` decimal(14,11) NOT NULL,
  `prec` decimal(6,2) NOT NULL,
  `cuenta` varchar(30) NOT NULL,
  `dispositivo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2016-10-02 01:39:37