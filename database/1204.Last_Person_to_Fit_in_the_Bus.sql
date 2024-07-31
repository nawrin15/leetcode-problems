----1204. Last Person to Fit in the Bus
SELECT q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING sum(q2.weight) <= 1000
ORDER BY Sum(q2.weight) DESC
LIMIT 1