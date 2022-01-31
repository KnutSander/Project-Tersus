SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS RFID_connection;
DROP TABLE IF EXISTS risk_group;
DROP TABLE IF EXISTS sick_leave;
DROP TABLE IF EXISTS achievement;
DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS sanitizer_station;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `sanitizer_station` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `location` TINYTEXT,
  `volume_capacity` INT,
  `volume_remaining` INT,
  `type` TINYTEXT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);
ALTER TABLE sanitizer_station AUTO_INCREMENT=1538;

CREATE TABLE `RFID_connection` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `UID` VARCHAR(255),
  `sanitizer_id` INT,
  `time_dispensed` TIMESTAMP,
  `time_spent` INT,
  `volume_used` INT
);

CREATE TABLE `employee` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `UID` VARCHAR(255) UNIQUE,
  `first_name` TINYTEXT,
  `last_name` TINYTEXT,
  `email` TINYTEXT,
  `department_id` INT,
  `risk_group_id` INT,
  `sick_days_left` INT,
  `shift_id` INT,
  `sick_day_id` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `sick_leave` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_id` INT,
  `duration` INT,
  `covid_related` BOOLEAN,
  `day_started` DATE
);

CREATE TABLE `department` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `goal_id` INT,
  `location` TINYTEXT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `risk_group` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT
);

CREATE TABLE `achievement` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_id` INT,
  `department_id` INT,
  `name` TINYTEXT,
  `value` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `goal` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `description` TEXT,
  `has_been_achieved` BOOLEAN,
  `value` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

ALTER TABLE `RFID_connection` ADD FOREIGN KEY (`sanitizer_id`) REFERENCES `sanitizer_station` (`id`);

ALTER TABLE `RFID_connection` ADD FOREIGN KEY (`UID`) REFERENCES `employee` (`UID`);

ALTER TABLE `employee` ADD FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);

ALTER TABLE `employee` ADD FOREIGN KEY (`risk_group_id`) REFERENCES `risk_group` (`id`);

ALTER TABLE `department` ADD FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`);

ALTER TABLE `achievement` ADD FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);

ALTER TABLE `achievement` ADD FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`);

ALTER TABLE `sick_leave` ADD FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`);
