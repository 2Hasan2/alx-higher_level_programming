-- Create the `faker` database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `faker`;

-- Use the `faker` database
USE `faker`;

-- Drop the `student` table if it exists
DROP TABLE IF EXISTS `student`;

-- Create the `student` table
CREATE TABLE `student` (
    `student_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `major` VARCHAR(50) NOT NULL
);

-- Generate and insert fake data into the `student` table
INSERT INTO `student` (`name`, `major`)
SELECT 
    CONCAT(first_name, ' ', last_name),
    CASE 
        WHEN major_choice = 1 THEN 'Computer Science'
        WHEN major_choice = 2 THEN 'Electrical Engineering'
        WHEN major_choice = 3 THEN 'Biology'
        WHEN major_choice = 4 THEN "Software Engineering"
        ELSE 'Chemistry'
    END AS major
FROM (
    SELECT 
        (SELECT SUBSTRING(MD5(RAND()) FROM 1 FOR 5)) AS first_name,
        (SELECT SUBSTRING(MD5(RAND()) FROM 1 FOR 5)) AS last_name,
        FLOOR(RAND() * 5) + 1 AS major_choice
    FROM 
        information_schema.tables
) AS fake_data
LIMIT 100;

-- Output success message
SELECT 'Fake data generated successfully!' AS 'Status';
