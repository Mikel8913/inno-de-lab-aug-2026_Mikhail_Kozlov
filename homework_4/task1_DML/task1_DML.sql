--Задание 1: DML
-- 1. Вставить двух сотрудников 
insert into Employees (FirstName, LastName, Department, Salary) values 
('James', 'Williams', 'HR', 55000.00),
('Ashley', 'Taylor', 'Finance', 53000.00);

-- 2. Выбрать всех сотрудников
select * from Employees;

-- 3. Выбрать только FirstName и LastName сотрудников из отдела 'IT'
select FirstName, LastName
from Employees
where Department = 'IT';

-- 4. Обновить Salary 'Alice Smith' до 65000.00
update Employees
set Salary = 65000.00
where FirstName = 'Alice' and LastName = 'Smith';

-- 5. Удалить сотрудника 'Eve Davis'
delete from employees
where FirstName = 'Eve' and LastName = 'Davis';

-- 6. Проверить все изменения, используя SELECT * FROM Employees;
select * from Employees;

