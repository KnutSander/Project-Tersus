SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS RFID_connections;
DROP TABLE IF EXISTS risk_group;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sanitizer_stations;
DROP TABLE IF EXISTS compliance;

SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE `sanitizer_stations` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `location` TINYTEXT,
  `volume_capacity` INT,
  `volume_remaning` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `RFID_connections` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `UID` VARCHAR(255),
  `sanitizer_id` INT,
  `time_dispensed` TIMESTAMP,
  `time_spent` INT,
  `volume_used` INT
);

CREATE TABLE `employees` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `UID` VARCHAR(255) UNIQUE,
  `first_name` TINYTEXT,
  `last_name` TINYTEXT,
  `department_id` INT,
  `risk_group_id` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `risk_group` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT
);

CREATE TABLE `departments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `location` TINYTEXT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `compliance` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `department_id` INT,
  `risk_group_id` INT,
  `perc_in_risk_group` FLOAT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

ALTER TABLE `RFID_connections` ADD FOREIGN KEY (`sanitizer_id`) REFERENCES `sanitizer_stations` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

ALTER TABLE `compliance` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`risk_group_id`) REFERENCES `risk_group` (`id`);

ALTER TABLE `RFID_connections` ADD FOREIGN KEY (`UID`) REFERENCES `employees` (`UID`);
