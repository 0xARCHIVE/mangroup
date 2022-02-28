SELECT product.product_id, product.name, SUM(orders.quantity)
FROM product, orders
WHERE product.product_id=orders.product_id AND orders.dispatch_date > add_months(SYSDATE, -12)
GROUP BY product.product_id, product.name
