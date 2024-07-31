---1341. Movie Rating
(
    select u.name as results 
    from MovieRating as r inner join Users as u on r.user_id = u.user_id
    Group By u.user_id
    Order By count(r.movie_id) desc, u.name limit 1
) 
union all
(
    select m.title as results
    from movies as m inner join MovieRating as r on m.movie_id = r.movie_id
    where created_at like '2020-02-%'
    Group By m.title
    Order By avg(r.rating) desc, m.title limit 1
)