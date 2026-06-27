CREATE TABLE airports(
    airport_code VARCHAR(3) PRIMARY KEY,
    airport_name VARCHAR(100)NOT NULL,
    city VARCHAR(50)NOT NULL,
    country VARCHAR(50)NOT NULL,
    region VARCHAR(50)NOT NULL,
    latitude DECIMAL(9,6)NOT NULL,
    longitude DECIMAL(9,6)NOT NULL

)