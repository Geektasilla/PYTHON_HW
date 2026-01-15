-- Databases 2025: Домашнее задание 11
--  База данных с доступом на запись:

-- Создать кастомные функции
-- Расчет площади круга
-- Создайте функцию для расчета площади круга, если известен его радиус.
-- Используйте формулу для расчета площади круга. S = pi*r**2
-- Где:
-- S — площадь круга,
-- r — радиус круга,
-- ​π≈3.14159, используйте функцию PI(), которая возвращает это число
DELIMITER //
CREATE FUNCTION circle_area(radius DECIMAL(10,2))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
	RETURN PI()*POW(radius, 2);
END //
DELIMITER ;

#SELECT circle_area();

-- 2. Функция для расчета гипотенузы треугольника.
-- Создайте функцию для расчета гипотенузы прямоугольного треугольника, если известны длины его катетов.
-- Используйте формулу для расчета гипотенузы прямоугольного треугольника
-- Где:
-- c — длина гипотенузы прямоугольного треугольника,
-- a, b — длины его катетов

DELIMITER //
CREATE FUNCTION calculate_hypotenuse(a DECIMAL(10, 2), b DECIMAL(10, 2))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
	RETURN SQRT(POW(a, 2) + POW(b, 2));
END //
DELIMITER ;

#SELECT calculate_hypotenuse();

