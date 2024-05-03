-- Create Database perfumes_db
CREATE DATABASE perfumes_db;
SHOW databases;

-- Get access to the database
USE perfumes_db:

-- Create the table perfumes within the database
CREATE TABLE perfumes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Brand VARCHAR(50),
    Size_ml INT,
    Price_eur DECIMAL(10, 2),
    Gender CHAR(1)
    );

-- Add all the initial data corresponding to the attributes
INSERT INTO perfumes (ID, Name, Brand, Size_ml, Price_eur, Gender) VALUES
(1, 'Paradoxe', 'Prada', 90, 148, 'F'),
(2, 'Good Girl', 'Carolina Herrera', 80, 139, 'F'),
(3, 'Idole', 'Lancome', 100, 141, 'F'),
(4, 'J’adore', 'Dior', 100, 152, 'F'),
(5, 'Be Delicious', 'DKNY', 50, 74, 'F'),
(6, 'Sauvage', 'Dior', 100, 169, 'M'),
(7, 'Bleu', 'Chanel', 100, 144, 'M'),
(8, 'Eros', 'Versace', 100, 110, 'M'),
(9, 'Armani Code', 'Armani', 120, 145, 'M'),
(10, 'Allure', 'Chanel', 100, 142, 'M');