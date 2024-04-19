CREATE DATABASE IF NOT EXISTS AirBnB;

USE AirBnB;

CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(30) NOT NULL,
    bio TEXT,
    country VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Booking (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

-- -- insert
-- INSERT INTO User (email, bio, country) VALUES ('hasan@gmail.com', 'I am a software engineer', 'Bangladesh');

-- -- Booking
-- INSERT INTO Booking (user_id, check_in, check_out) VALUES (1, '2021-01-01', '2021-01-10');

-- -- Rooms
-- INSERT INTO Rooms (user_id, name, description, price) VALUES (1, 'Room 1', 'This is a room', 100.00);

SELECT * 
FROM User
WHERE id = 1;