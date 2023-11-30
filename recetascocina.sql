-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2023 a las 04:32:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `recetascocina`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `idCategoria` int(11) NOT NULL,
  `Categoria` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`idCategoria`, `Categoria`) VALUES
(1, 'Cerdo'),
(2, 'Empanadas'),
(3, 'Ensaladas'),
(4, 'Guisos'),
(5, 'Helados'),
(6, 'Pastas'),
(7, 'Pizzas / Tartas'),
(8, 'Pollo'),
(9, 'Postres'),
(10, 'Tortas'),
(11, 'Vegetarianas'),
(12, 'Carne'),
(13, 'Veganas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `idFavorito` int(11) NOT NULL,
  `idReceta` int(5) NOT NULL,
  `idUsuario` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `favoritos`
--

INSERT INTO `favoritos` (`idFavorito`, `idReceta`, `idUsuario`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 3),
(5, 3, 2),
(6, 3, 4),
(7, 4, 3),
(8, 4, 5),
(9, 5, 1),
(10, 5, 4),
(11, 6, 2),
(12, 7, 3),
(13, 8, 4),
(14, 9, 5),
(15, 10, 1),
(16, 10, 2),
(17, 10, 3),
(18, 10, 4),
(19, 10, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recetas`
--

CREATE TABLE `recetas` (
  `idReceta` int(11) NOT NULL,
  `NombreReceta` varchar(25) NOT NULL,
  `Ingredientes` text DEFAULT NULL,
  `Receta` text DEFAULT NULL,
  `Porciones` int(5) NOT NULL,
  `urlImagen` varchar(100) NOT NULL,
  `TiempoMin` int(5) NOT NULL,
  `idUsuario` int(5) NOT NULL,
  `idCategoria` int(5) NOT NULL,
  `dificultad` enum('Fácil','Intermedio','Difícil') DEFAULT NULL,
  `fechaCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `recetas`
--

INSERT INTO `recetas` (`idReceta`, `NombreReceta`, `Ingredientes`, `Receta`, `Porciones`, `urlImagen`, `TiempoMin`, `idUsuario`, `idCategoria`, `dificultad`, `fechaCreacion`) VALUES
(1, 'Receta1', 'ZZ Ingredientes para la receta 1 <br> lero 1 <br> caro 2', 'Instrucciones de la receta 1', 4, '/static/imagenes/image1.jpg', 30, 1, 1, 'Fácil', '2023-10-01 00:00:00'),
(2, 'Receta2', 'Ingredientes para la receta 2 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 2', 6, '/static/imagenes/image2.jpg', 45, 2, 2, 'Intermedio', '2023-10-02 00:00:00'),
(3, 'Receta3', 'Ingredientes para la receta 3 <br> Ingrediente 1 <br> caro 2', 'Instrucciones de la receta 3', 2, '/static/imagenes/image3.jpg', 20, 3, 3, 'Fácil', '2023-10-03 00:00:00'),
(4, 'Receta4', 'Ingredientes para la receta 4 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 4', 8, '/static/imagenes/image4.jpg', 60, 4, 4, 'Difícil', '2023-10-04 00:00:00'),
(5, 'Receta5', 'Ingredientes para la receta 5 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 5', 3, '/static/imagenes/image5.jpg', 40, 5, 5, 'Intermedio', '2023-10-05 00:00:00'),
(6, 'Receta6', 'Ingredientes para la receta 6 <br> lero 1 <br> Ingrediente 2', 'Instrucciones de la receta 6', 4, '/static/imagenes/image6.jpg', 35, 1, 6, 'Fácil', '2023-10-06 00:00:00'),
(7, 'Receta7', 'Ingredientes para la receta 7 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 7', 6, '/static/imagenes/image7.jpg', 50, 2, 7, 'Intermedio', '2023-10-07 00:00:00'),
(8, 'Receta8', 'Ingredientes para la receta 8 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 8', 2, '/static/imagenes/image8.jpg', 25, 3, 8, 'Fácil', '2023-10-08 00:00:00'),
(9, 'Receta9', 'Ingredientes para la receta 9 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 9', 8, '/static/imagenes/image9.jpg', 55, 4, 9, 'Difícil', '2023-10-09 00:00:00'),
(10, 'Receta10', 'Ingredientes para la receta 10 <br> Ingrediente 1 <br> Ingrediente 2', 'Instrucciones de la receta 10', 3, '/static/imagenes/image10.jpg', 30, 5, 10, 'Intermedio', '2023-10-10 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `NombreUsuario` varchar(15) NOT NULL,
  `Nombre` varchar(15) NOT NULL,
  `Apellido` varchar(15) NOT NULL,
  `Nacimiento` int(5) NOT NULL,
  `correoElectronico` varchar(30) NOT NULL,
  `Hash` varchar(64) NOT NULL,
  `Genero` varchar(11) NOT NULL,
  `Admin` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `NombreUsuario`, `Nombre`, `Apellido`, `Nacimiento`, `correoElectronico`, `Hash`, `Genero`, `Admin`) VALUES
(1, 'admin', 'Nombre', 'Apellido', 1991, 'admin@example.com', 'a7a057f8baea8970e940cec1bfc35ca3fc9a4f934570157178ef3aed98b7ad6a', 'Masculino', 1),
(2, 'usuario1', 'Nombre1', 'Apellido1', 1990, 'usuario1@example.com', '6212322273285378477212120347811095149337405249061541661322299034', 'Masculino', 0),
(3, 'usuario2', 'Nombre2', 'Apellido2', 1995, 'usuario2@example.com', '5441755061551569310833758766352157795329471374355996975667032133', 'Femenino', 0),
(4, 'usuario3', 'Nombre3', 'Apellido3', 1985, 'usuario3@example.com', '4537901544141539281720688772988080928072754524784469352421214552', 'Masculino', 0),
(5, 'usuario4', 'Nombre4', 'Apellido4', 1992, 'usuario4@example.com', '6141790587410847588387914396693155216098926337612666765353988653', 'Femenino', 0),
(6, 'usuario5', 'Nombre5', 'Apellido5', 1998, 'usuario5@example.com', '6126456093550928635209027254548095356707836722398397860852546249', 'Masculino', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`idCategoria`);

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`idFavorito`),
  ADD KEY `idReceta` (`idReceta`),
  ADD KEY `idUsuario` (`idUsuario`);

--
-- Indices de la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`idReceta`),
  ADD KEY `idCategoria` (`idCategoria`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `idCategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `idFavorito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `recetas`
--
ALTER TABLE `recetas`
  MODIFY `idReceta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`idReceta`) REFERENCES `recetas` (`idReceta`) ON DELETE CASCADE,
  ADD CONSTRAINT `favoritos_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE;

--
-- Filtros para la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD CONSTRAINT `recetas_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `categorias` (`idCategoria`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
