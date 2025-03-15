# Exercise 1 — Tasks

Find the title of each film

```sql
SELECT title from movies
```

Find the director of each film

```sql
SELECT director from movies
```

Find the title and director of each film

```sql
SELECT title, director from movies
```

Find the title and year of each film

```sql
SELECT title, year from movies
```

Find all the information about each film

```sql
SELECT * from movies
```

![alt text](image.png)

# Exercise 2 — Tasks

![alt text](image-1.png)

Find the movie with a row id of 6

```sql
SELECT title FROM movies WHERE id = 6;
```

Find the movies released in the years between 2000 and 2010

```sql
SELECT title FROM movies WHERE year >= 2000 AND year <= 2010;

SELECT title FROM movies WHERE year BETWEEN 2000 and 2010;
```

Find the movies not released in the years between 2000 and 2010

```sql
SELECT title FROM movies WHERE year NOT BETWEEN 2000 and 2010;
```

Find the first 5 Pixar movies and their release year

```sql
SELECT title FROM movies where id between 1 and 5;
```

![alt text](image-2.png)

# Exercise 3 — Tasks

![alt text](image-3.png)

Find all the Toy Story movies

```sql
SELECT * FROM movies WHERE title LIKE "toy story%";
```

Find all the movies directed by John Lasseter

```sql
SELECT * FROM movies WHERE director LIKE "John Lasseter";
```

Find all the movies (and director) not directed by John Lasseter

```sql
SELECT * FROM movies WHERE director NOT LIKE "John Lasseter";
```

Find all the WALL-\* movies

```sql
SELECT * FROM movies WHERE title LIKE "wall-%";

```

![alt text](image-4.png)

# Exercise 4 — Tasks

![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)

List all directors of Pixar movies (alphabetically), without duplicates

```sql
SELECT DISTINCT director FROM movies order by director asc;
```

List the last four Pixar movies released (ordered from most recent to least)

```sql
SELECT * FROM movies ORDER BY year desc LIMIT 4 ;
```

List the first five Pixar movies sorted alphabetically

```sql
SELECT * FROM movies order by title, year asc limit 5;
```

List the next five Pixar movies sorted alphabeticall

```sql
SELECT * FROM movies order by title, year asc limit 5 offset 5;
```

# Review 1 — Tasks

![alt text](image-8.png)

List all the Canadian cities and their populations

```sql
SELECT * FROM north_american_cities where country like "canada";
```

Order all the cities in the United States by their latitude from north to south

```sql
SELECT * FROM north_american_cities where country like "united states" order by latitude desc;
```

List all the cities west of Chicago, ordered from west to east

```sql
SELECT * FROM north_american_cities
order by longitude asc
limit 6;


SELECT *
FROM north_american_cities
WHERE longitude < (SELECT longitude FROM nort_american_cities WHERE city = "Chicago")
Order by longitude

```

List the two largest cities in Mexico (by population)

```sql
SELECT * FROM north_american_cities
where country = "Mexico"
order by population desc
limit 2;

```

List the third and fourth largest cities (by population) in the United States and their population

```sql
SELECT * FROM north_american_cities
where country = "United States"
order by population desc
limit 2 offset 2;
```

# On joining

![alt text](image-11.png)

![alt text](image-12.png)

## 1. both data visible:

![alt text](image-13.png)

## 2. mixing data types not allowed

## 3. having table without primary key not permitted

- unique
- not null
- only one in a table

## 4. repeating group not permitted

## second normal from

![alt text](image-14.png)

## third normal from

![alt text](image-15.png)

# Exercise 6 — Tasks

![alt text](image-9.png)
![alt text](image-10.png)

Find the domestic and international sales for each movie

```sql
SELECT *
FROM movies
INNER JOIN Boxoffice
on Movies.id = Boxoffice.Movie_id;
```

Show the sales numbers for each movie that did better internationally rather than domestically

```sql
SELECT *
FROM movies
INNER JOIN Boxoffice
on Movies.id = Boxoffice.Movie_id
WHERE boxoffice.international_sales>boxoffice.domestic_sales;
```

List all the movies by their ratings in descending order

```sql
SELECT *
FROM movies
INNER JOIN Boxoffice
on Movies.id = Boxoffice.Movie_id
ORDER BY boxoffice.rating desc;
```

![alt text](image-16.png)

# Exercise 7 — Tasks

![alt text](image-17.png)
![alt text](image-18.png)

Find the list of all buildings that have employees

```sql
SELECT DISTINCT building
FROM employees;
```

Find the list of all buildings and their capacity

```sql
SELECT *
FROM buildings;
```

List all buildings and the distinct employee roles in each building (including empty buildings)

```sql
SELECT DISTINCT
buildings.building_name, employees.role
FROM buildings
LEFT JOIN employees
on  buildings.building_name = employees.building;
```

![alt text](image-19.png)

# Exercise 8 — Tasks

![alt text](image-20.png)

Find the name and role of all employees who have not been assigned to a building

```sql
SELECT * FROM employees
where building is null;
```

Find the names of the buildings that hold no employees

```sql
SELECT * FROM buildings
left join employees
on buildings.building_name = employees.building
where employees.building is null;
```

![alt text](image-21.png)

# Exercise 9 — Tasks

![alt text](image-22.png)
![alt text](image-23.png)

List all movies and their combined sales in millions of dollars

```sql
SELECT * , ((domestic_sales + international_sales)/1000000) as gross_sales
FROM movies
inner join boxoffice
on id = movie_id;
```

List all movies and their ratings in percent

```sql
SELECT *, (rating*10) as ratings
FROM movies
inner join boxoffice
on id = movie_id;
```

List all movies that were released on even number years

```sql
SELECT *
FROM movies
inner join boxoffice
on id = movie_id
where year%2 = 0;
```

![alt text](image-24.png)

# Exercise 10 — Tasks

![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)

Find the longest time that an employee has been at the studio

```sql
SELECT *, Max(years_employed)
FROM employees;
```

For each role, find the average number of years employed by employees in that role

```sql
SELECT Role,  avg(years_employed)
FROM employees
group by role;
```

Find the total number of employee years worked in each building

```sql
SELECT building,  sum(years_employed)
FROM employees
group by building;
```

![alt text](image-28.png)

# Exercise 11 — Tasks

![alt text](image-29.png)

Find the number of Artists in the studio (without a HAVING clause)

```sql
SELECT role, count(role)
FROM employees
where role = "Artist";
```

Find the number of Employees of each role in the studio

```sql
SELECT role, count(role)
FROM employees
group by role;
```

Find the total number of years employed by all Engineers

```sql
SELECT *, sum(years_employed)
FROM employees
where role = "Engineer";
```

![alt text](image-30.png)

# Exercise 12 — Tasks

![alt text](image-31.png)
![alt text](image-32.png)
![alt text](image-33.png)

Find the number of movies each director has directed

```sql
SELECT director, count(director)
FROM movies
group by director;
```

Find the total domestic and international sales that can be attributed to each director

```sql
SELECT *, sum(domestic_sales + international_sales) as gross
FROM movies
INNER JOIN boxoffice
on id = movie_id
group by director;
```

![alt text](image-34.png)
