SELECT C.customer_name, C.country, SUM(O.total_amount) AS total_spent
FROM Orders O
JOIN Customers C ON O.customer_id = C.customer_id
GROUP BY C.customer_name, C.country;
