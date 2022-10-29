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


