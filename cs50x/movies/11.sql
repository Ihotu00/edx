select movies.title
from movies
left join ratings
on movies.id = ratings.movie_id
where id in(
    select movie_id
    from stars
    where person_id =(
        select id
        from people
        where name = "Chadwick Boseman"
    )
)
order by ratings.rating desc
limit 5