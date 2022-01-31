SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS RFID_connections;
DROP TABLE IF EXISTS achievements;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employee_working_shifts;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS sanitizer_stations;
DROP TABLE IF EXISTS shifts;
DROP TABLE IF EXISTS statistics;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `sanitizer_stations` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `location` TINYTEXT,
  `is_empty` BOOLEAN,
  `alcohol_content` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `RFID_connections` (
  `UID` INT PRIMARY KEY AUTO_INCREMENT,
  `sanitizer_id` INT,
  `time_dispensed` TIMESTAMP,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `employees` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `first_name` TINYTEXT,
  `last_name` TINYTEXT,
  `department_id` INT,
  `sick_days` INT,
  `shift_id` INT,
  `salary` INT,
  `meals_served` INT,
  `hospital_bed_days` INT,
  `type_of_transport` TINYTEXT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `departments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `goal_id` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `statistics` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `department_id` INT,
  `time_calculated` TIMESTAMP,
  `metric_1` INT,
  `metric_2` INT,
  `metric_3` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `achievements` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_id` INT,
  `department_id` INT,
  `name` TINYTEXT,
  `value` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `goals` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `description` TEXT,
  `has_been_achieved` BOOLEAN,
  `value` INT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `shifts` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` TINYTEXT,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

CREATE TABLE `employee_working_shifts` (
  `shift_id` INT,
  `employee_id` INT,
  `hours_worked` INT,
  `day_started` DATE,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP
);

ALTER TABLE `RFID_connections` ADD FOREIGN KEY (`sanitizer_id`) REFERENCES `sanitizer_stations` (`id`);

ALTER TABLE `RFID_connections` ADD FOREIGN KEY (`UID`) REFERENCES `employees` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

ALTER TABLE `employee_working_shifts` ADD FOREIGN KEY (`shift_id`) REFERENCES `shifts` (`id`);

ALTER TABLE `employee_working_shifts` ADD FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`);

ALTER TABLE `departments` ADD FOREIGN KEY (`goal_id`) REFERENCES `goals` (`id`);

ALTER TABLE `achievements` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

ALTER TABLE `achievements` ADD FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`);

ALTER TABLE `statistics` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);
