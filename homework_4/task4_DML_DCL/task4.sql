-- Задание 4. DML/DCL 
-- 1. Увеличить Salary всех сотрудников в отделе 'HR' на 10%. 
update employees
set salary = salary + (salary * 0.10)
where department = 'HR';

-- 2. Обновить Department любого сотрудника с Salary выше 70000.00 
-- на 'Senior IT'
update employees
set department = 'Senior IT'
where salary > 70000.00;

-- 3. Удалить всех сотрудников, которые не назначены ни на один проект в 
-- таблице EmployeeProjects. Подсказка: Используйте подзапрос NOT 
-- EXISTS или LEFT JOIN 
delete from employees emp
where not exists (
	select 1
	from employeeProjects empl
	where empl.employeeID = emp.employeeID
);

-- 4. В рамках одной транзакции, вставить новый проект и назначить на 
-- него двух существующих сотрудников с определенным количеством 
-- HoursWorked в EmployeeProjects. 
BEGIN;

WITH new_project AS (
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('Database_Upgrade', 150000.00, '2026-07-01', NULL)
    RETURNING ProjectID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    tab1.EmployeeID,
    new_project.ProjectID,
    tab1.HoursWorked
FROM new_project
CROSS JOIN (VALUES (2, 40), (4, 30)) AS tab1(EmployeeID, HoursWorked);

COMMIT;

SELECT * FROM Employees;
SELECT * FROM Projects;
SELECT * FROM EmployeeProjects;