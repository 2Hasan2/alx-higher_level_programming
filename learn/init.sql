CREATE DATABASE IF NOT EXISTS Zoo_DB;

USE Zoo_DB;

CREATE TABLE IF NOT EXISTS animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    species VARCHAR(20) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Unknown')
);

-- INSERT INTO animals (name, species, age, gender) VALUES("mike", "dog", 100, "Male");

SELECT * FROM animals;
