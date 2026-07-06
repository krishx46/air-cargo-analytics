INSERT INTO warehouse.fact_shipments
(
    shipment_id,
    customer_id,
    flight_number,
    weather_id,
    date_id,
    weight_kg,
    volume_cbm,
    revenue_usd,
    shipment_status,
    priority_level
)

SELECT

    s.shipment_id,

    s.customer_id,

    s.flight_number,

    w.weather_id,

    d.date_id,

    s.weight_kg,

    s.volume_cbm,

    s.revenue_usd,

    s.shipment_status,

    s.priority_level

FROM shipments s

JOIN warehouse.dim_date d
ON s.shipment_date = d.full_date

JOIN flights f
ON s.flight_number = f.flight_number

JOIN warehouse.dim_weather w
ON f.origin_airport = w.airport_code
AND s.shipment_date = w.weather_date;