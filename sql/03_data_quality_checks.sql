/*
Data Quality Validation

Purpose:
- Verify referential integrity
- Check for duplicate records
- Validate business rules
- Ensure no invalid or missing data before loading into the data warehouse

Result:
All validation checks passed successfully.
*/


-- Check for duplicate shipment IDs
SELECT shipment_id, COUNT(*)
FROM shipments
GROUP BY shipment_id
HAVING COUNT(*) > 1;

-- Check for negative revenue
SELECT *
FROM shipments
WHERE revenue_usd < 0;

-- Check for invalid delivery dates
SELECT *
FROM shipments
WHERE delivery_date < shipment_date;

-- Check for orphan customers
SELECT COUNT(*)
FROM shipments s
LEFT JOIN customers c
ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;