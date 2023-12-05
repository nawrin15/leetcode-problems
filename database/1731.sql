--- 1731. The Number of Employees Which Report to Each Employee ---
select E.employee_id, E.name, COUNT(R.employee_id) reports_count, ROUND(AVG(R.age)) average_age
FROM Employees E INNER JOIN Employees R ON 
E.employee_id = R.reports_to 
GROUP BY E.employee_id, E.name 
ORDER BY E.employee_id