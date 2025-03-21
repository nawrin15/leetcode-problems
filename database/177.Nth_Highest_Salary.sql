CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N -1;
RETURN (
    select distinct(salary)
    from Employee
    order by salary desc
    Limit 1 offset N
);
END