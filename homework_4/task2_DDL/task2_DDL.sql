-- Задание 2: DDL 
-- 1. Создать новую таблицу с именем Departments со столбцами: 
-- DepartmentID (SERIAL PRIMARY KEY), DepartmentName 
-- (VARCHAR(50), UNIQUE, NOT NULL), Location (VARCHAR(50)). 
create table Departments (
	DepartmentID SERIAL primary key,
	DepartmentName VARCHAR(50) unique not null,
	Location VARCHAR(50)
	);

-- 2. Изменить таблицу Employees, добавив новый столбец с именем 
-- Email (VARCHAR(100))
alter table Employees
add column Email VARCHAR(100);

-- 3. Заполнить столбец Email для всех текущих сотрудников 
-- уникальными значениями (например, через UPDATE)
update employees
set Email = Lower(FirstName) || '.' || Lower(LastName) || '@company.com';

-- 4. Добавить ограничение UNIQUE к столбцу Email в таблице 
-- Employees
alter table employees 
add constraint unique_emloyee_email unique (Email);

-- 5. Переименовать столбец Location в таблице Departments в OfficeLocation
alter table departments 
rename column location to OfficeLocation;

select * from employees;
select * from departments;