DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS shipments;
DROP TABLE IF EXISTS weather;

CREATE TABLE airports(
    airport_code VARCHAR(3) PRIMARY KEY,
    airport_name VARCHAR(100)NOT NULL,
    city VARCHAR(50)NOT NULL,
    country VARCHAR(50)NOT NULL,
    region VARCHAR(50)NOT NULL,
    latitude DECIMAL(9,6)NOT NULL,
    longitude DECIMAL(9,6)NOT NULL

);
CREATE TABLE aircraft(
    aircraft_id INT PRIMARY KEY,
    aircraft_type VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    capacity_kg INT NOT NULL,
    range_km INT NOT NULL,
    manufacture_year INT NOT NULL,
    aircraft_status VARCHAR(20) NOT NULL
    CHECK (aircraft_status IN 
    ('Active', 'Maintenance', 'Retired')
    )
);
CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    industry VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE    NOT NULL,
    phone VARCHAR(20) NOT NULL
);
CREATE TABLE flights(
    flight_number VARCHAR(10) PRIMARY KEY,
    origin_airport VARCHAR(3) NOT NULL,
    destination_airport VARCHAR(3) NOT NULL,
    aircraft_id INT NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    arrival_time TIMESTAMP NOT NULL,
    distance_km INT NOT NULL,
    flight_status VARCHAR(20) NOT NULL
    CHECK (
        flight_status IN (
            'Scheduled', 'On Time', 'Delayed', 'Cancelled', 'Landed')
    ),
    FOREIGN KEY (origin_airport) REFERENCES airports(airport_code),
    FOREIGN KEY (destination_airport) REFERENCES airports(airport_code),
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id)
);
CREATE TABLE shipments(
    shipment_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    flight_number VARCHAR(10) NOT NULL,
    shipment_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    cargo_type VARCHAR(50) NOT NULL,
    weight_kg DECIMAL(10,2) NOT NULL
    CHECK (weight_kg > 0),
    volume_cbm DECIMAL(10,2) NOT NULL,
    revenue_usd DECIMAL(12,2) NOT NULL
    CHECK (revenue_usd >= 0),
    shipment_status VARCHAR(20) NOT NULL
    CHECK(
        shipment_status IN (
            'Pending', 'In Transit', 'Delivered', 'Delayed', 'Cancelled')
    ),
    priority_level VARCHAR(20) NOT NULL
    CHECK(
        priority_level IN (
            'Low', 'Medium', 'High', 'Critical')
    ),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (flight_number) REFERENCES flights(flight_number)
);
CREATE TABLE weather(
    weather_id INT PRIMARY KEY,
    airport_code VARCHAR(3) NOT NULL,
    weather_date DATE NOT NULL,
    weather_condition VARCHAR(50) NOT NULL,
    temperature_c DECIMAL(5,2) NOT NULL,
    visibility_km DECIMAL(5,2) NOT NULL,
    wind_speed_kmh DECIMAL(5,2) NOT NULL,
    delay_risk VARCHAR(20) NOT NULL,
    FOREIGN KEY (airport_code) REFERENCES airports(airport_code)
);