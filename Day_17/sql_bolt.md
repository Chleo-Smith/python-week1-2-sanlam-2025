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

```

List the two largest cities in Mexico (by population)

```sql

```

List the third and fourth largest cities (by population) in the United States and their population

```sql

```
