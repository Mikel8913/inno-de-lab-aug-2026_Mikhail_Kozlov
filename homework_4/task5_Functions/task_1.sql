-- Задание 5. Функции и представления
-- 1. Функция CalculateAnnualBonus (10% от Salary)
create or replace function CalculateAnnualBonus (
	employee_id int,
	salary decimal(10,2)
)
returns decimal(10,2) as $$
begin
	return salary * 0.10;
end;
$$ language plpgsql;

-- 2. Использовать эту функцию в операторе SELECT, чтобы увидеть 
-- потенциальный бонус для каждого сотрудника.
select
	employeeID,
	FirstName,
	LastName,
	Salary,
	CalculateAnnualBonus(employeeID, salary) as AnnualBonus
from employees
order by EmployeeID;

-- 3. Представление (View): Создать представление с именем 
-- IT_Department_View, которое показывает EmployeeID, 
-- FirstName, LastName и Salary только для сотрудников из отдела 
-- 'IT'
create or replace view IT_Department_View as
select EmployeeID, FirstName, LastName, salary
from Employees
where department = 'IT';

-- 4. Выбрать данные из вашего представления IT_Department_View.
select * from IT_Department_View;

-- Добавил двух сотрудников в 'IT'
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Emma', 'Watson', 'IT', 72000.00),
('Liam', 'Garcia', 'IT', 68000.00);




