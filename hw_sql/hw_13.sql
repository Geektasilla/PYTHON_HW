# 1. Выберите только те строки из таблицы suppliers, где company имеет значение Supplier A

SELECT id, company
FROM northwind.suppliers
WHERE company = "Supplier A";

# 2. Вывести все строки там, где purchase_order_id не указано.
# При этом дополнительно создать столбец total_price как произведение quantity * unit_price

SELECT *, quantity * unit_cost AS total_price
FROM northwind.purchase_order_details
WHERE purchase_order_id is NULL;

# 3. Выведите какая дата будет через 51 день
SELECT NOW() + INTERVAL 51 DAY;

# 4.  Посчитайте количество уникальных заказов purchase_order_id
SELECT DISTINCT purchase_order_id
FROM northwind.purchase_order_details;

# 5. Выведите все столбцы таблицы order_details, 
# а также дополнительный столбец payment_method из таблицы purchase_orders.
# Оставьте только заказы для которых известен payment_method

SELECT 
	od.*, 
	po.payment_method
FROM 
	northwind.order_details AS od
JOIN 
	northwind.purchase_orders AS po
ON 
	od.purchase_order_id = po.id
WHERE 
	po.payment_method IS NOT NULL;