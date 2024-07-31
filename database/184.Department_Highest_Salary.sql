
select dept.name as Department, emp.name as Employee, emp.salary as Salary
from Employee emp join Department dept on dept.id = emp.departmentId 
where (emp.salary, emp.departmentId) in (
    SELECT MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId);


