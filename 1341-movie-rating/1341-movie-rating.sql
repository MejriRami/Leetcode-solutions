-- Step 1: Find user who rated the most movies
WITH user_counts AS (
    SELECT 
        u.name,
        COUNT(*) AS cnt
    FROM MovieRating m
    JOIN Users u ON m.user_id = u.user_id
    GROUP BY u.user_id, u.name
),
top_user AS (
    SELECT name
    FROM user_counts
    WHERE cnt = (SELECT MAX(cnt) FROM user_counts)
    ORDER BY name
    LIMIT 1
),

-- Step 2: Find movie with highest average rating in Feb 2020
movie_avg AS (
    SELECT 
        mv.title,
        AVG(m.rating) AS avg_rating
    FROM MovieRating m
    JOIN Movies mv ON m.movie_id = mv.movie_id
    WHERE m.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mv.movie_id, mv.title
),
top_movie AS (
    SELECT title
    FROM movie_avg
    WHERE avg_rating = (SELECT MAX(avg_rating) FROM movie_avg)
    ORDER BY title
    LIMIT 1
)

-- Step 3: Combine results
SELECT name AS results FROM top_user
UNION ALL
SELECT title AS results FROM top_movie;
