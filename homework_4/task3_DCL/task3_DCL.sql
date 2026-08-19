-- Задание 3: DCL 
-- 1. Создать нового пользователя PostgreSQL (роль) с именем hr_user и 
-- паролем
create user hr_user with login password 'Secure123!';

-- 2. Предоставить hr_user право SELECT на таблицу Employees
grant select on Employees to hr_user;

-- 3. Тест 1. В новой сессии подключиться как hr_user и попытаться 
-- выполнить SELECT * FROM Employees;. (Должно сработать). 

-- Тест 2. Под hr_user попытаться выполнить INSERT нового 
-- сотрудника (должна возникнуть ошибка доступа).  

-- 4. Как пользователь-администратор, предоставить hr_user права 
-- INSERT и UPDATE на таблицу Employees. 
grant insert, update on employees to hr_user;

-- Предоставил права на использование последовательности
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;

-- 5. Тест 3. Как hr_user, попробовать выполнить INSERT и UPDATE 
-- сотрудника. (Теперь должно сработать)