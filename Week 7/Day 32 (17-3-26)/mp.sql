-- Fetch all records
SELECT * FROM pizza_sales;

-- Total Revenue
SELECT SUM(total_price) AS TOTAL_REVENUE FROM pizza_sales;

-- Total Orders
SELECT COUNT(DISTINCT order_id) AS TOTAL_ORDERS FROM pizza_sales;

-- Total Pizzas Sold
SELECT SUM(quantity) AS TOTAL_PIZZAS_SOLD FROM pizza_sales;

-- Average Order Value
SELECT SUM(total_price)/COUNT(DISTINCT order_id) AS AVERAGE_ORDER_VALUE FROM pizza_sales;

-- Average Pizzas per Order
SELECT CAST(SUM(quantity) AS FLOAT)/COUNT(DISTINCT order_id) AS AVERAGE_PIZZAS_PER_ORDER FROM pizza_sales;

-- Daily Trends
SELECT DATENAME(WEEKDAY, order_date) AS DAY_NAME,
       COUNT(DISTINCT order_id) AS TOTAL_ORDERS
FROM pizza_sales
GROUP BY DATENAME(WEEKDAY, order_date)
ORDER BY TOTAL_ORDERS DESC;

-- Monthly Trends
SELECT DATENAME(MONTH, order_date) AS MONTH_NAME,
       COUNT(DISTINCT order_id) AS TOTAL_ORDERS
FROM pizza_sales
GROUP BY DATENAME(MONTH, order_date)
ORDER BY TOTAL_ORDERS DESC;

-- Percentage of Pizza Sales by Category
SELECT pizza_category,
       SUM(total_price) AS TOTAL_SALES,
       SUM(total_price)*100.0/(SELECT SUM(total_price) FROM pizza_sales) AS REVENUE_PERCENTAGE
FROM pizza_sales
GROUP BY pizza_category
ORDER BY REVENUE_PERCENTAGE DESC;

-- Percentage of Pizza Sales by Size
SELECT pizza_size,
       SUM(total_price) AS TOTAL_SALES,
       SUM(total_price)*100.0/(SELECT SUM(total_price) FROM pizza_sales) AS REVENUE_PERCENTAGE
FROM pizza_sales
GROUP BY pizza_size
ORDER BY REVENUE_PERCENTAGE DESC;

-- Total Pizzas Sold by Category
SELECT pizza_category, SUM(quantity) AS TOTAL_PIZZAS_SOLD
FROM pizza_sales
GROUP BY pizza_category
ORDER BY TOTAL_PIZZAS_SOLD DESC;

-- Top 5 Best Sellers by Revenue
SELECT TOP 5 pizza_name, SUM(total_price) AS REVENUE
FROM pizza_sales
GROUP BY pizza_name
ORDER BY REVENUE DESC;

-- Top 5 Best Sellers by Quantity
SELECT TOP 5 pizza_name, SUM(quantity) AS QUANTITY_SOLD
FROM pizza_sales
GROUP BY pizza_name
ORDER BY QUANTITY_SOLD DESC;

-- Top 5 Best Sellers by Orders
SELECT TOP 5 pizza_name, COUNT(DISTINCT order_id) AS TOTAL_ORDERS
FROM pizza_sales
GROUP BY pizza_name
ORDER BY TOTAL_ORDERS DESC;

-- Bottom 5 Sellers by Revenue
SELECT TOP 5 pizza_name, SUM(total_price) AS REVENUE
FROM pizza_sales
GROUP BY pizza_name
ORDER BY REVENUE ASC;

-- Bottom 5 Sellers by Quantity
SELECT TOP 5 pizza_name, SUM(quantity) AS QUANTITY_SOLD
FROM pizza_sales
GROUP BY pizza_name
ORDER BY QUANTITY_SOLD ASC;

-- Bottom 5 Sellers by Orders
SELECT TOP 5 pizza_name, COUNT(DISTINCT order_id) AS TOTAL_ORDERS
FROM pizza_sales
GROUP BY pizza_name
ORDER BY TOTAL_ORDERS ASC;
