-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-11-2025 a las 21:10:30
-- Versión del servidor: 10.1.34-MariaDB
-- Versión de PHP: 5.6.37

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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

CREATE TABLE `enfermedad` (
  `idENFERMEDAD` int(11) NOT NULL,
  `nomENFERMEDAD` varchar(70) COLLATE utf8_unicode_ci NOT NULL,
  `descENFERMEDAD` text COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invernadero`
--

CREATE TABLE `invernadero` (
  `idINVERNADERO` int(11) NOT NULL,
  `nomINVERNADERO` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `superfINVERNADERO` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipoCultivoINVERNADERO` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fechaCreacINVERNADERO` date DEFAULT NULL,
  `responsableINVERNADERO` varchar(90) COLLATE utf8_unicode_ci DEFAULT NULL,
  `capacINVERNADERO` int(11) DEFAULT NULL,
  `sistRiegoINVERNADERO` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `idUSUARIO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUSUARIO` int(11) NOT NULL,
  `nomUSUARIO` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apellidoUSUARIO` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `emailUSUARIO` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `userUSUARIO` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `passwUSUARIO` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `enfermedad`
--
ALTER TABLE `enfermedad`
  ADD PRIMARY KEY (`idENFERMEDAD`);

--
-- Indices de la tabla `invernadero`
--
ALTER TABLE `invernadero`
  ADD PRIMARY KEY (`idINVERNADERO`),
  ADD KEY `fk_invernaderos_usuario` (`idUSUARIO`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUSUARIO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `enfermedad`
--
ALTER TABLE `enfermedad`
  MODIFY `idENFERMEDAD` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `invernadero`
--
ALTER TABLE `invernadero`
  MODIFY `idINVERNADERO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUSUARIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `invernadero`
--
ALTER TABLE `invernadero`
  ADD CONSTRAINT `fk_invernaderos_usuario` FOREIGN KEY (`idUSUARIO`) REFERENCES `usuario` (`idUSUARIO`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
