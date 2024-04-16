-- create database is not exist 
CREATE DATABASE IF NOT EXISTS `faker`;

-- start use the database with name
USE faker;

-- create table if not exist
-- CREATE TABLE IF NOT EXISTS student (
--     student_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(20) NOT NULL,
--     major VARCHAR(20)
-- );

-- -- this to modifies column in table
-- ALTER TABLE student MODIFY COLUMN major VARCHAR(20) DEFAULT 'undefind';

-- -- insert data in the table
-- INSERT INTO student (name) VALUES("jack");

-- -- show all column in the tanle
-- SELECT * FROM student;

-- -- show all table column name that have student_id = 2
-- SELECT name FROM student WHERE student_id = 2;


-- udate data in the table 
-- UPDATE student
-- SET major = "software dev"
-- WHERE major = "Bio"
-- AND name = "hasan";


-- -- Delete rows from a Table

-- DELETE FROM  student
-- WHERE name = 'jack';

SELECT *
FROM student
-- filter it
-- <> not 
WHERE major <> "Electrical Engineering"
-- if in (.....)
AND major IN ("Computer Science", "Software Engineering")
-- between num to num
AND student_id BETWEEN 20 AND 60
-- list it by order
ORDER BY major, student_id
-- limit 5 student
LIMIT 30;