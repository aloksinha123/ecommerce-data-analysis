-- Total revenue from all orders
SELECT SUM(quantity * unit_price) AS total_revenue
FROM order_items;
-- ans total revenue is 140400.00

-- 2. Top 5 customers by revenue
SELECT
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.customer_name
ORDER BY revenue DESC;

-- 3. Top 5 products by quantity sold
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

-- 4. Revenue by city

SELECT
    c.city,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.city
ORDER BY revenue DESC;


-- 5. repeat customer
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS number_of_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT o.order_id) > 1
ORDER BY number_of_orders DESC;

