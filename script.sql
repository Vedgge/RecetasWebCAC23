DROP DATABASE IF EXISTS `recetascocina`;

CREATE DATABASE recetascocina;

USE recetascocina;

DROP TABLE IF EXISTS `recetas`;
DROP TABLE IF EXISTS `usuarios`;
DROP TABLE IF EXISTS `categorias`;
DROP TABLE IF EXISTS `favoritos`;

CREATE TABLE `recetascocina`.`categorias` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `Categoria` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`idCategoria`)
);

CREATE TABLE `recetascocina`.`usuarios` (
`idUsuario` INT NOT NULL AUTO_INCREMENT,
`Nombre` VARCHAR(15) NOT NULL,
`Apellido` VARCHAR(15) NOT NULL,
`Nacimiento` int(5) NOT NULL,
`correoElectrónico` VARCHAR(30) NOT NULL,
`Hash` VARCHAR(64) NOT NULL,
`Genero` VARCHAR(11) NOT NULL,
PRIMARY KEY (`idUsuario`)
);

CREATE TABLE `recetascocina`.`recetas` (
`idReceta` INT NOT NULL AUTO_INCREMENT,
`NombreReceta` VARCHAR(25) NOT NULL,
`claveJSON` VARCHAR(15) NOT NULL,
`Porciones` int(5) NOT NULL,
`Tiempo(min)` int(5) NOT NULL,
`idUsuario` int(5) NOT NULL,
`idCategoria` int(5) NOT NULL,
`dificultad` ENUM ('Fácil','Intermedio','Difícil'),
PRIMARY KEY (`idReceta`),
FOREIGN KEY (`idCategoria`) REFERENCES `categorias` (`idCategoria`) ON DELETE CASCADE
);

CREATE TABLE `recetascocina`.`favoritos` (
  `idFavorito` INT NOT NULL AUTO_INCREMENT,
  `idReceta` int(5) NOT NULL,
  `idUsuario` int(5) NOT NULL,
  PRIMARY KEY (`idFavorito`),
  FOREIGN KEY (`idReceta`) REFERENCES `recetas` (`idReceta`) ON DELETE CASCADE,
  FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE
);

INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Cerdo');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Empanadas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Ensaladas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Guisos');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Helados');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Pastas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Pizzas / Tartas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Pollo');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Postres');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Tortas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Vegetarianas');
INSERT INTO `recetascocina`.`categorias` (`Categoria`) VALUES ('Carne');

