-- Create Database perfumes_db
CREATE DATABASE perfumes_db;
SHOW databases;

-- Get access to the database
USE perfumes_db;

-- Create the table perfumes within the database
CREATE TABLE perfumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Brand VARCHAR(50),
    Size_ml INT,
    Price_eur DECIMAL(10, 2),
    Gender CHAR(1)
    );

-- Add all the initial data corresponding to the attributes
INSERT INTO perfumes (Name, Brand, Size_ml, Price_eur, Gender) VALUES
('Paradoxe', 'Prada', 90, 148, 'F'),
('Good Girl', 'Carolina Herrera', 80, 139, 'F'),
('Idole', 'Lancome', 100, 141, 'F'),
('J’adore', 'Dior', 100, 152, 'F'),
('Be Delicious', 'DKNY', 50, 74, 'F'),
('Sauvage', 'Dior', 100, 169, 'M'),
('Bleu', 'Chanel', 100, 144, 'M'),
('Eros', 'Versace', 100, 110, 'M'),
('Armani Code', 'Armani', 120, 145, 'M'),
('Allure', 'Chanel', 100, 142, 'M');