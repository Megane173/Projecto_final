-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 03-11-2025 a las 04:02:58
-- Versión del servidor: 11.5.2-MariaDB
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemainvernaderos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedad`
--

DROP TABLE IF EXISTS `enfermedad`;
CREATE TABLE IF NOT EXISTS `enfermedad` (
  `idENFERMEDAD` int(11) NOT NULL AUTO_INCREMENT,
  `nomENFERMEDAD` varchar(70) NOT NULL,
  `descENFERMEDAD` text DEFAULT NULL,
  PRIMARY KEY (`idENFERMEDAD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invernadero`
--

DROP TABLE IF EXISTS `invernadero`;
CREATE TABLE IF NOT EXISTS `invernadero` (
  `idINVERNADERO` int(11) NOT NULL AUTO_INCREMENT,
  `nomINVERNADERO` varchar(100) NOT NULL,
  `superfINVERNADERO` varchar(10) DEFAULT NULL,
  `tipoCultivoINVERNADERO` varchar(15) DEFAULT NULL,
  `fechaCreacINVERNADERO` date DEFAULT NULL,
  `responsableINVERNADERO` varchar(90) DEFAULT NULL,
  `capacINVERNADERO` int(11) DEFAULT NULL,
  `sistRiegoINVERNADERO` varchar(20) DEFAULT NULL,
  `idUSUARIO` int(11) NOT NULL,
  PRIMARY KEY (`idINVERNADERO`),
  KEY `fk_invernadero_usuario` (`idUSUARIO`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Volcado de datos para la tabla `invernadero`
--

INSERT INTO `invernadero` (`idINVERNADERO`, `nomINVERNADERO`, `superfINVERNADERO`, `tipoCultivoINVERNADERO`, `fechaCreacINVERNADERO`, `responsableINVERNADERO`, `capacINVERNADERO`, `sistRiegoINVERNADERO`, `idUSUARIO`) VALUES
(1, 'algo', '1000', 'Café', '2025-06-11', 'Yo', 1256, 'Automatizado', 2),
(2, 'algo', '1000', 'Café', '2025-06-11', 'Yo', 1256, 'Automatizado', 1),
(3, 'Amirtch', '1320', 'Tomate', '2024-07-04', 'Jaimito', 805, 'Por goteo', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `idUSUARIO` int(11) NOT NULL AUTO_INCREMENT,
  `nomUSUARIO` varchar(45) DEFAULT NULL,
  `apellidoUSUARIO` varchar(45) DEFAULT NULL,
  `emailUSUARIO` varchar(100) DEFAULT NULL,
  `userUSUARIO` varchar(30) NOT NULL,
  `passwUSUARIO` varchar(30) NOT NULL,
  PRIMARY KEY (`idUSUARIO`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUSUARIO`, `nomUSUARIO`, `apellidoUSUARIO`, `emailUSUARIO`, `userUSUARIO`, `passwUSUARIO`) VALUES
(1, NULL, NULL, NULL, 'flosh', '123456'),
(2, NULL, NULL, NULL, 'f', '1');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `invernadero`
--
ALTER TABLE `invernadero`
  ADD CONSTRAINT `fk_invernadero_usuario` FOREIGN KEY (`idUSUARIO`) REFERENCES `usuario` (`idUSUARIO`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
