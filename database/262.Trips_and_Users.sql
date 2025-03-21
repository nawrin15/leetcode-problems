
--1
SELECT request_at as Day, ROUND(COUNT(IF(status != 'completed', True, NULL)) / COUNT(*),2) AS 'Cancellation Rate'
FROM Trips
WHERE request_at BETWEEN "2013-10-01" and "2013-10-03"
AND client_id in (SELECT users_id FROM Users WHERE banned = 'No')
AND driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
GROUP BY request_at

--2
select t.Request_at Day,
       ROUND((count(IF(t.status!='completed',TRUE,null))/count(*)),2) as 'Cancellation Rate'
from Trips t where 
t.Client_Id in (Select Users_Id from Users where Banned='No') 
and t.Driver_Id in (Select Users_Id from Users where Banned='No')
and t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at;