INSERT INTO sanitizer_stations(name, location, volume_capacity, volume_remaning, created_at, updated_at) VALUES ("Alcohol gel", "Front entry", 200, 200, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO risk_group(name) VALUES ("High"), ("Medium"), ("Low");
INSERT INTO departments(name, location, created_at, updated_at) VALUES ("Sales", "Floor 1", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO employees(UID, first_name, last_name, department_id, risk_group_id, created_at, updated_at) VALUES ("E0040100019D0CA1", "Samuel", "Engel", 1, 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP );
INSERT INTO RFID_connections(UID, sanitizer_id, time_dispensed, time_spent, volume_used) VALUES ("E0040100019D0CA1", 1, CURRENT_TIMESTAMP, 5, 1);
INSERT INTO compliance(department_id, risk_group_id, created_at, updated_at) VALUES (1, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
