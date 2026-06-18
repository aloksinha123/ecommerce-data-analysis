SELECT
    c.customer_name,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 10;