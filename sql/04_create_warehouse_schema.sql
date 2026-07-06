CREATE SCHEMA warehouse;

CREATE TABLE warehouse.dim_customer (

    customer_id INT PRIMARY KEY,

    customer_name VARCHAR(150),

    customer_type VARCHAR(50),

    industry VARCHAR(50),

    country VARCHAR(100),

    city VARCHAR(100)

);
CREATE TABLE warehouse.dim_airport (

    airport_code VARCHAR(3) PRIMARY KEY,

    airport_name VARCHAR(150),

    city VARCHAR(100),

    country VARCHAR(100),

    region VARCHAR(100),

    latitude DECIMAL(8,4),

    longitude DECIMAL(8,4)

);
CREATE TABLE warehouse.dim_flight (

    flight_number VARCHAR(10) PRIMARY KEY,

    origin_airport VARCHAR(3),

    destination_airport VARCHAR(3),

    aircraft_id INT,

    distance_km DECIMAL(8,2),

    departure_time TIMESTAMP,

    arrival_time TIMESTAMP,

    flight_status VARCHAR(30)

);
CREATE TABLE warehouse.dim_weather (

    weather_id INT PRIMARY KEY,

    airport_code VARCHAR(3),

    weather_date DATE,

    weather_condition VARCHAR(50),

    temperature_c DECIMAL(5,2),

    visibility_km DECIMAL(5,2),

    wind_speed_kmh DECIMAL(5,2),

    delay_risk VARCHAR(20)

);
CREATE TABLE warehouse.dim_date (

    date_id INT PRIMARY KEY,

    full_date DATE,

    day INT,

    month INT,

    month_name VARCHAR(20),

    quarter INT,

    year INT,

    day_of_week VARCHAR(20),

    is_weekend BOOLEAN

);

CREATE TABLE warehouse.fact_shipments (

    shipment_id INT PRIMARY KEY,

    customer_id INT NOT NULL,

    flight_number VARCHAR(10) NOT NULL,

    weather_id INT NOT NULL,

    date_id INT NOT NULL,

    weight_kg DECIMAL(10,2),

    volume_cbm DECIMAL(10,2),

    revenue_usd DECIMAL(12,2),

    shipment_status VARCHAR(30),

    priority_level VARCHAR(30)

);