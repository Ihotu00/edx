SELECT name from songs WHERE artist_id = (
    SELECT id from artists where name = "Post Malone"
)