-- FILE: task_5.sql
INSERT INTO Customers (customer_name, email, address)
VALUES ('Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
ON DUPLICATE KEY UPDATE
customer_name = VALUES(customer_name),
address = VALUES(address);

