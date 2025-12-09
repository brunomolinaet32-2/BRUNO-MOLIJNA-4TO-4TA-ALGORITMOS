-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-12-2025 a las 16:27:55
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `farmacity`
--
CREATE DATABASE IF NOT EXISTS `farmacity` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `farmacity`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicamentos`
--

DROP TABLE IF EXISTS `medicamentos`;
CREATE TABLE `medicamentos` (
  `ID` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `medicamentos`
--

INSERT INTO `medicamentos` (`ID`, `nombre`, `categoria`, `precio`, `stock`) VALUES
(1, 'Acetaminofén', 'Analgésicos', '250.00', 100),
(2, 'Naproxeno', 'Antiinflamatorios', '50.00', 100),
(3, 'Azitromicina', 'Antibióticos', '30.00', 50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE `ventas` (
  `ID` int(10) UNSIGNED NOT NULL,
  `ID_Medicamento` int(10) UNSIGNED NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`ID`, `ID_Medicamento`, `fecha`, `cantidad`) VALUES
(1, 1, '2025-11-01', 1),
(2, 2, '2025-05-02', 2),
(3, 1, '2025-05-03', 3),
(4, 3, '2025-12-20', 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `medicamentos`
--
ALTER TABLE `medicamentos`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Medicamento` (`ID_Medicamento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `medicamentos`
--
ALTER TABLE `medicamentos`
  MODIFY `ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`ID_Medicamento`) REFERENCES `medicamentos` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
