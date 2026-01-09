
#Таблица order_details
#1. Для каждого product_id выведите inventory_id, а также предыдущий и последующей inventory_id по убыванию quantity
SELECT product_id, inventory_id,
lag(inventory_id) over(partition by product_id order by quantity DESC) as lag_inventory_id,
lead(inventory_id) over(partition by product_id order by quantity DESC) as lead_inventory_id
FROM northwind.order_details;

#2. Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST VALUE.  
# Вывести order_id и полученные значения.

SELECT order_id, unit_price,
min(unit_price) over(partition by order_id) as min_unit_price,
max(unit_price) over(partition by order_id) as max_unit_price,
FIRST_VALUE(unit_price) over (partition by order_id order by unit_price) as min_unit_price2,
FIRST_VALUE(unit_price) over (partition by order_id order by unit_price DESC) as max_unit_price2
FROM northwind.order_details;

# 3 Выведите order_id и столбец с разницей между  unit_price для каждого заказа и минимальным unit_price в рамках одного заказа.
# Задачу решить двумя способами - с помощью First VAlue и MIN

SELECT 
	order_id, unit_price,
	unit_price - min(unit_price) over (partition by order_id) as diff_min_unit_price,
	unit_price - first_value(unit_price) over (partition by order_id order by unit_price) as diff_firs_unit_price
FROM northwind.order_details;


#4 Присвойте ранг каждой строке используя RANK по убыванию quantity

SELECT *,
rank() over(order by quantity DESC) as rank_num
FROM northwind.order_details;

#5  Из предыдущего запроса выберите только строки с рангом до 10 включительно
SELECT *
FROM
	(SELECT *, rank() over(order by quantity DESC) as rank_num
	FROM northwind.order_details) t
WHERE rank_num <= 10;
  



FROM northwind.order_details;
