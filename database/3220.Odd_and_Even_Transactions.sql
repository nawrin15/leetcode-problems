SELECT  transaction_date,
SUM(case when amount % 2 = 1 THEN amount else 0 end) as odd_sum,
SUM(case when amount % 2 = 0 THEN amount else 0 end) as even_sum
FROM transactions
Group by transaction_date
order by transaction_date