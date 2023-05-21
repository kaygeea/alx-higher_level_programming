-- Import temperatures table into the hbtn_0c_0 DB from CLI using "mysql -u root -p hbtn_0c_0 < temperatures.sql"
-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
