-- 1 Вывести id департамента , в котором работает сотрудник, 
-- в зависимости от Id сотрудника

USE 101025_Viktoria;
SELECT * FROM 101025_Viktoria.employees4;
DELIMITER //
CREATE PROCEDURE get_id_departments(IN emp_id INT)
BEGIN
	SELECT department_id FROM 101025_Viktoria.employees4
    WHERE id = emp_id;
    
END //
DELIMITER ;
CALL get_id_departments(2);


-- 2 Создайте хранимую процедуру get_employee_age, 
-- которая принимает id сотрудника (IN-параметр) 
-- и возвращает его возраст через OUT-параметр.

USE 101025_Viktoria;
SELECT * FROM 101025_Viktoria.employees4;
DELIMITER //
CREATE PROCEDURE get_employee_age(IN emp_id INT, OUT emp_age INT)
BEGIN
	SELECT age INTO emp_age FROM 101025_Viktoria.employees4
    WHERE id = emp_id;
END //
DELIMITER ;
CALL get_employee_age(2, @result_emp_age2);
SELECT @result_emp_age2;
    
-- 3 Создайте хранимую процедуру decrease_salary, 
-- которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.

USE 101025_Viktoria;
SELECT * FROM 101025_Viktoria.employees4;

DELIMITER //
CREATE PROCEDURE decrease_salary(INOUT current_salary DECIMAL(10,2))
BEGIN
	SET current_salary = current_salary * 0.9;
END //
DELIMITER ;

SET @initial_salary = 5500;
CALL decrease_salary(@initial_salary);
SELECT @initial_salary AS DecreaseSalary;