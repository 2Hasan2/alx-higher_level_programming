-- Create the `faker` database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `faker`;

-- Use the `faker` database
USE `faker`;

-- Drop the `student` table if it exists
DROP TABLE IF EXISTS `student`;

-- Create the `student` table
CREATE TABLE `student` (
    `student_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(50) NOT NULL
);

-- Generate and insert fake data into the `student` table
INSERT INTO `student` (`name`, `major`)
SELECT 
    CONCAT(first_name, ' ', last_name) AS name,
    CASE 
        WHEN major_choice = 1 THEN 'Computer Science'
        WHEN major_choice = 2 THEN 'Electrical Engineering'
        WHEN major_choice = 3 THEN 'Biology'
        WHEN major_choice = 4 THEN 'Software Engineering'
        WHEN major_choice = 5 THEN 'Chemistry'
        WHEN major_choice = 6 THEN 'Physics'
        WHEN major_choice = 7 THEN 'Mathematics'
        ELSE "Civil Engineering"
    END AS major
FROM (
    SELECT 
        (SELECT first_name FROM (SELECT 'John' AS first_name UNION ALL SELECT 'Jane' UNION ALL SELECT 'Michael' UNION ALL SELECT 'Emily' UNION ALL SELECT 'David' UNION ALL SELECT 'Sarah' UNION ALL SELECT 'Christopher' UNION ALL SELECT 'Emma' UNION ALL SELECT 'Daniel' UNION ALL SELECT 'Olivia' UNION ALL SELECT 'Matthew' UNION ALL SELECT 'Sophia' UNION ALL SELECT 'Andrew' UNION ALL SELECT 'Ava' UNION ALL SELECT 'James' UNION ALL SELECT 'Isabella') AS first_names ORDER BY RAND() LIMIT 1) AS first_name,
        (SELECT last_name FROM (SELECT 'Doe' AS last_name UNION ALL SELECT 'Smith' UNION ALL SELECT 'Johnson' UNION ALL SELECT 'Brown' UNION ALL SELECT 'Taylor' UNION ALL SELECT 'Anderson' UNION ALL SELECT 'Thomas' UNION ALL SELECT 'Jackson' UNION ALL SELECT 'White' UNION ALL SELECT 'Harris' UNION ALL SELECT 'Martin' UNION ALL SELECT 'Thompson' UNION ALL SELECT 'Garcia' UNION ALL SELECT 'Martinez' UNION ALL SELECT 'Robinson') AS last_names ORDER BY RAND() LIMIT 1) AS last_name,
        FLOOR(RAND() * 10) + 1 AS major_choice -- Adjusted to 10 choices
    FROM
        (SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5) AS t1,
        (SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5) AS t2
) AS fake_data
LIMIT 100; -- Adjust the limit to 100

SELECT * FROM student;

-- Output success message
SELECT 'Fake data generated successfully!' AS 'Status';
