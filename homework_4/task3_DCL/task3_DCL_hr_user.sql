-- Тест 1. В новой сессии подключиться как hr_user и попытаться 
-- выполнить SELECT * FROM Employees;. (Должно сработать). 
select * from employees;

-- Тест 2. Под hr_user попытаться выполнить INSERT нового 
-- сотрудника (должна возникнуть ошибка доступа).  
 INSERT INTO Employees (FirstName, LastName, Department, Salary)
 VALUES ('Test', 'User', 'Finance', 40000.00);

-- 5. Тест 3. Как hr_user, попробовать выполнить INSERT и UPDATE 
-- сотрудника. (Теперь должно сработать)

INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Test', 'User', 'Finance', 40000.00);

UPDATE Employees SET Salary = 45500.00 WHERE FirstName = 'Test';