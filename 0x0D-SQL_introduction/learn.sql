CREATE DATABASE IF NOT EXISTS `learn`;

USE learn;

CREATE TABLE IF NOT EXISTS  student (
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);



ALTER TABLE student ADD gpa DECIMAL(3, 2);

DESCRIBE student;
