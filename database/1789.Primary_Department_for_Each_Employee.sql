----1789. Primary Department for Each Employee
----1
select a.employee_id, a.department_id
from Employee a
where primary_flag='Y' or (
   select count(*)
   from Employee e
   where a.employee_id = employee_id
) = 1
-----2
SELECT employee_id, department_id 
FROM Employee
WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id 
FROM Employee 
GROUP BY employee_id
HAVING COUNT(employee_id) = 1