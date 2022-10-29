-- ttps://sqlbolt.com/lesson/select_queries_introduction
-- SQL Lesson 1

SELECT Title FROM movies
SELECT director FROM movies
SELECT title, director FROM movies
SELECT title, year FROM movies
SELECT * FROM movies

-- SQL Lesson 2
SELECT title FROM movies WHERE Id=6 
SELECT Title FROM movies WHERE year >= 2000 AND year <=2010
SELECT Title FROM movies WHERE year NOT BETWEEN 2000 AND 2010
SELECT Title FROM movies WHERE ID<6

-- SQL Lesson 3
SELECT Title FROM movies WHERE Title LIKE "%Toy Story%"
SELECT Title FROM movies WHERE director = "John Lasseter"
SELECT Title, director FROM movies WHERE director != "John Lasseter"
SELECT Title FROM movies WHERE Title LIKE "Wall-%"

-- SQL Lesson 4
SELECT DISTINCT director FROM movies ORDER BY director ASC
SELECT Title FROM movies ORDER BY year DESC LIMIT 4
SELECT Title FROM movies ORDER BY title ASC LIMIT 5
SELECT title FROM movies ORDER BY title ASC LIMIT 5 OFFSET 5

-- SQL Lesson 5
--class_work

-- SQL Lesson 6
SELECT title, domestic_sales, international_sales FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id

SELECT title, domestic_sales, international_sales 
  FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id WHERE Domestic_sales < International_sales

SELECT title, 	Rating
  FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id ORDER BY Rating DESC

-- SQL Lesson 7

SELECT DISTINCT building FROM employees
SELECT Building_name, Capacity FROM Buildings 
SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees
    ON building_name = building

-- SQL Lesson 8
SELECT Name, Role FROM employees WHERE Building IS NULL
SELECT DISTINCT building_name FROM buildings 
  LEFT JOIN employees ON building_name = building
    WHERE role IS NULL

--SQL Lesson 9
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id

SELECT title, Rating * 10 AS ratings_in_percent
FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id

SELECT title, year FROM movies WHERE year % 2 = 0

--SQL Lesson 10
SELECT MAX(years_employed) as Max_years_employed FROM employees

SELECT role, AVG(years_employed) as Average_years_employed FROM employees GROUP BY role

SELECT building, SUM(years_employed) as Total_years_employed FROM employees GROUP BY building

--SQL Lesson 11

SELECT role, COUNT(*) as Number_of_artists FROM employees WHERE role = "Artist"

SELECT role, COUNT(*) FROM employees GROUP BY role

SELECT role, SUM(years_employed) FROM employees GROUP BY role HAVING role = "Engineer"

--SQL Lesson 12
SELECT director, COUNT(id) as Num_movies_directed FROM movies GROUP BY director

SELECT director, SUM(domestic_sales + international_sales) as Cumulative_sales_from_all_movies
    FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id
        GROUP BY director

--SQL Lesson 13
INSERT INTO movies VALUES (4, "Toy Story 4", "	John Lasseter", 2022, 99)
INSERT INTO BoxOffice VALUES (4, 8.7, 340000000, 270000000)

--SQL Lesson 14
UPDATE movies SET director = "John Lasseter" WHERE id = 2
UPDATE movies SET Year = 1999 WHERE title = "Toy Story 2"
UPDATE movies SET title = "Toy Story 3", director = "Lee Unkrich" WHERE id = 11

--SQL Lesson 15
DELETE FROM movies WHERE year <= 2005
DELETE FROM movies WHERE Director = 'Andrew Stanton'

--SQL Lesson 16
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER)

--SQL Lesson 17
ALTER TABLE Movies ADD COLUMN Aspect_ratio FLOAT DEFAULT 1.23
ALTER TABLE Movies ADD COLUMN Language TEXT DEFAULT 'English'

--SQL Lesson 18
DROP TABLE Movies
DROP TABLE BoxOffice


