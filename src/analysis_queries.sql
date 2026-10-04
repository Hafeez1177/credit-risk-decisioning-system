-- Inventory & demand analytics

-- Demand by category
SELECT Category, SUM("Demand Units") AS demand
FROM inventory_demand GROUP BY Category ORDER BY demand DESC;

-- Stockout rate by region
SELECT Region, ROUND(100.0*SUM(Stockout)/COUNT(*),2) AS stockout_rate
FROM inventory_demand GROUP BY Region ORDER BY stockout_rate DESC;

-- Reorder candidates
SELECT SKU, Category, Region, "Demand Units", "On Hand Units",
       "Inbound Units", "Safety Stock Units", "Projected Gap"
FROM inventory_demand
WHERE "Projected Gap" > 0
ORDER BY "Projected Gap" DESC;

-- Demand by channel
SELECT Channel, SUM("Demand Units") AS demand
FROM inventory_demand GROUP BY Channel ORDER BY demand DESC;

-- Weekly demand
SELECT Week, SUM("Demand Units") AS demand
FROM inventory_demand GROUP BY Week ORDER BY Week;
