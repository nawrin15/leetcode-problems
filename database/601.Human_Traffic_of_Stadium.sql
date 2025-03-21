with t as ( select t1.id , t1.visit_date , t1.people , 
            id - row_number() OVER(ORDER BY id) as grp
       from stadium t1
       where people >= 100 
          )
select t.id, t.visit_date ,t.people
from t 
where grp in ( select grp from t group by grp having count(*) >=3  )


--2 
SELECT
    id,
    visit_date,
    people
FROM (
SELECT
    id,
    visit_date,
    people,
    LEAD(id, 1) OVER (ORDER BY id) next_id,
    LEAD(id, 2) OVER (ORDER BY id) next_2_id,
    LAG(id, 1) OVER (ORDER BY id) prior_id,
    LAG(id, 2) OVER (ORDER BY id) prior_2_id
FROM
    Stadium
WHERE 
    people >= 100
) BASE
WHERE 
    (id - prior_id = 1 AND next_id - id = 1)
OR
    (id - prior_id = 1 AND prior_id - prior_2_id = 1)
OR
    (next_id - id = 1 AND next_2_id - next_id = 1)
;

--3
WITH ptr AS (
    SELECT id, visit_date, people,
           LEAD(id, 1) OVER (ORDER BY id) AS next_id_1,
           LEAD(id, 2) OVER (ORDER BY id) AS next_id_2,
           LAG(id, 1) OVER (ORDER BY id) AS prev_id_1,
           LAG(id, 2) OVER (ORDER BY id) AS prev_id_2
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM ptr
WHERE (next_id_1 = id + 1 AND next_id_2 = id + 2)
   OR (prev_id_1 = id - 1 AND next_id_1 = id + 1)
   OR (prev_id_2 = id - 2 AND prev_id_1 = id - 1)
ORDER BY visit_date;