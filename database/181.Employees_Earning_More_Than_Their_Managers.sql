select emp.name as Employee
from Employee emp
where emp.salary > (
    select salary 
    from Employee
    where id = emp.managerId )


SELECT a.name as Employee
FROM Employee a
JOIN Employee b
ON a.managerId = b.id
WHERE a.salary > b.salary