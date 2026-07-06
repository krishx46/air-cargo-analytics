INSERT INTO warehouse.dim_customer (
    customer_id,
    customer_name,
    customer_type,
    industry,
    country,
    city
)
SELECT
    customer_id,
    customer_name,
    customer_type,
    industry,
    country,
    city
FROM customers;
INSERT INTO warehouse.dim_airport (
    airport_code,
    airport_name,
    city,
    country,
    region,
    latitude,
    longitude
)
SELECT
    airport_code,
    airport_name,
    city,
    country,
    region,
    latitude,
    longitude
FROM airports;
INSERT INTO warehouse.dim_flight (
    flight_number,
    origin_airport,
    destination_airport,
    aircraft_id,
    distance_km,
    departure_time,
    arrival_time,
    flight_status
)
SELECT
    flight_number,
    origin_airport,
    destination_airport,
    aircraft_id,
    distance_km,
    departure_time,
    arrival_time,
    flight_status
FROM flights;
INSERT INTO warehouse.dim_weather (
    weather_id,
    airport_code,
    weather_date,
    weather_condition,
    temperature_c,
    visibility_km,
    wind_speed_kmh,
    delay_risk
)
SELECT
    weather_id,
    airport_code,
    weather_date,
    weather_condition,
    temperature_c,
    visibility_km,
    wind_speed_kmh,
    delay_risk
FROM weather;
INSERT INTO warehouse.dim_dates
(
    date_id,
    full_date,
    day,
    month,
    month_name,
    quarter,
    year,
    day_of_week,
    is_weekend
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY shipment_date) AS date_id,
    shipment_date AS full_date,
    EXTRACT(DAY FROM shipment_date)::INT,
    EXTRACT(MONTH FROM shipment_date)::INT,
    TRIM(TO_CHAR(shipment_date, 'Month')),
    EXTRACT(QUARTER FROM shipment_date)::INT,
    EXTRACT(YEAR FROM shipment_date)::INT,
    TRIM(TO_CHAR(shipment_date, 'Day')),
    CASE
        WHEN EXTRACT(ISODOW FROM shipment_date) IN (6, 7)
        THEN TRUE
        ELSE FALSE
    END
FROM(
    SELECT DISTINCT shipment_date
    FROM shipments
)d;