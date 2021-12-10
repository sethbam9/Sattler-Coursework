import sqlite3

            #Table name
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    #col name  type  constraint
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);

SELECT * FROM flights # select all columns

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = "New York"

INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);

# Finding item in list
SELECT * FROM flights WHERE origin IN ("New York", "Lima");

# Wildcard is %
SELECT * FROM flights WHERE origin LIKE "%L%";

UPDATE flights
    SET duration = 430
    WHERE origin = "New York"
    AND destination = "London";

DELETE FROM flights WHERE destination = "Tokyo";


SELECT first, origin, destination
    FROM flights JOIN passengers
    ON passengers.flight_id = flights.id;
