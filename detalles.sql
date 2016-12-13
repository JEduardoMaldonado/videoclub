create database pelis;
use pelis;

CREATE TABLE datos (
  `id_dato` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `pelicula` VARCHAR(70) NULL,
  `formato` VARCHAR(70) NULL,
  `cliente` VARCHAR(70) NULL,
  `tiempo` VARCHAR(70) NOT NULL ,
  `total` VARCHAR(70) NOT NULL );
 
