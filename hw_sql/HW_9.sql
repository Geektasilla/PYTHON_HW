-- Таблица purchase_order_details
USE northwind;
SELECT * FROM northwind.purchase_order_details; 

-- 1. Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost

SELECT purchase_order_id,
MIN(unit_cost) over (PARTITION BY purchase_order_id) AS min_unit_cost, 
MAX(unit_cost) over (PARTITION BY purchase_order_id) AS max_unit_cost, 
AVG(unit_cost) over (PARTITION BY purchase_order_id) AS avg_unit_cost
FROM purchase_order_details;
#_________GROUP BY____________ 
SELECT purchase_order_id,
MIN(unit_cost) AS min_unit_cost, 
MAX(unit_cost) AS max_unit_cost, 
AVG(unit_cost) AS avg_unit_cost
FROM purchase_order_details
GROUP BY purchase_order_id;

-- 2.  Оставьте только уникальные строки из предыдущего запроса
SELECT DISTINCT purchase_order_id,
MIN(unit_cost) over (PARTITION BY purchase_order_id) AS min_unit_cost, 
MAX(unit_cost) over (PARTITION BY purchase_order_id) AS max_unit_cost, 
AVG(unit_cost) over (PARTITION BY purchase_order_id) AS avg_unit_cost
FROM purchase_order_details;

-- 3. Посчитайте стоимость продукта в заказе как quantity * unit_cost 
-- Выведите суммарную стоимость продуктов с помощью оконной функции 
-- Сделайте то же самое с помощью GROUP BY

SELECT DISTINCT
	product_id,
	SUM(unit_cost * quantity) over (PARTITION BY product_id) AS sum_cost
FROM purchase_order_details;

#---------GROUP BY-------------
SELECT 
	product_id,
	ROUND(SUM(quantity * unit_cost),2) AS sum_cost
FROM purchase_order_details
GROUP BY product_id;

-- 4. Посчитайте количество заказов по дате получения и posted_to_inventory 
-- Если оно превышает 1 то выведите '>1' в противном случае '=1'
-- Выведите purchase_order_id, date_received и вычисленный столбец

SELECT purchase_order_id, date_received,
CASE
    WHEN COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) > 1
    THEN '>1'
	ELSE '=1'
END AS orders_info
FROM (
SELECT DISTINCT purchase_order_id, date_received, posted_to_inventory
FROM purchase_order_details) orders_by_date;

