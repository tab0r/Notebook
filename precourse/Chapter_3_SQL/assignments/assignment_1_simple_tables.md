# Assignment: SQL on simple tables

## Objectives

- Use PostgreSQL (defaulting to SQLite if necessary).
- Create and dump tables.
- Populate tables.
- Build simple queries (SELECT, FROM, WHERE, CASE clauses).
- Build queries with aggregates (DISTINCT, COUNT, SUM, GROUP BY, HAVING, ORDER BY).
- Build complex queries on multiple tables: JOINs.

_______________________________________

## Questions & Answers

#### Instructions

Please write your answers in [your_answers.txt](your_answers.txt).
- If you feel comfortable in SQL, answer the questions in [your_answers.txt](your_answers.txt) directly. You will need the two tables `animals` and `pets` given below, but can skip the rest of this page.
- If you need extra guidance, follow the steps on this page which gives you more guidance in writing your queries.
- If you feel a need to brush up on SQL, go to the [extra resources](#extra-resources) section at the bottom of this assignment for great places to learn and practice in a more guided environment.

#### Our data
We will be working with the following toy data, organized in 2 tables ([animals table](../data/animals.csv) and [pets table](../data/pets.csv)).

<b>Table 1: animals</b>

| species   | vertebrate_class | appearance  | num_leg  |
| :-------: | :--------------: | :---------: | :------: |
| cat       | mammal           | fur         | 4        |
| rat       | mammal           | fur         | 4        |
| owl       | bird             | feathers    | 2        |
| snake     | reptile          | dry scales  | 0        |
| toad      | amphibian        | smooth skin | 4        |
| alligator | reptile          | dry scales  | 4        |

<b>Table 2: pets</b>

| name        | species | owner             | gender | Color         |
| :---------: | :----: | :----------------: | :----: | :-----------: |
| Nagini      | snake  | Lord Voldemort     | female | green         |
| Hedwig      | owl    | Harry Potter       | female | snow white    |
| Scabbers    | rat    | Ron Weasley        | male   | unspecified   |
| Pigwidgeon  | owl    | Ron Weasley        | male   | grey          |
| Crookshanks | cat    | Herminone Granger  | male   | ginger        |
| Mrs Norris  | cat    | Argus Filch        | female | dust-coloured |
| Trevor      | toad   | Neville Longbottom | male   | brown         |

Thanks to [Harry Potter Wiki](http://www.harrypotter.wikia.com) for all of this information!



### 0. Creating and exploring tables

[Here](../resources/create_sql_table.md) is a very simple workflow that you can adapt to any situation when you want to test your queries on toy data.


*Step 1:* Create a psql database and the tables.

1. Open Postgres

2. Create an `animalshp` database and check it was created.


*Step 2:* Creating your tables.

1. Let's enter the `animalshp` database to create the SQL tables. Check that the prompt now reads `animalshp=#`.

2. Create the animals table. Create the pets table. For now, they remain empty.


*Step 3:* Insert values in the tables.

1. Insert values by hand in the animals table (sorry!)

2. Insert values in the pets table from the `pets.csv` file in the `data` repository (it has a header).

3. Check the content of your tables, they should match Table 1 and Table 2 above.

  ```SQL
  SELECT * FROM pets;
  SELECT * FROM animals;
  ```

### 1. Simple queries on a single table: SELECT, FROM, WHERE, CASE clauses

1. Use the `WHERE` clause to show the appearance of 'rats'.

2. Use `IN` to check if an item is in a list and show the species for vertebrate_class in 'mammal' and 'amphibian'.

3. Use `BETWEEN xxx AND xxx` to show species that have more than 1 leg, but fewer than 3 legs.

4. Use `LIKE 'X'` to show species that have an appearance that starts with 'f'.

5. Use `CASE` to show pet names and a column to indicate whether the pet's name is long or short (a long name is strictly more than 6 character long). How about adding a filter to select only female pets?


### 2. Build queries with aggregates (DISTINCT, COUNT, SUM, GROUP BY, HAVING, ORDER BY)

1. Use `DISTINCT` to list the species that can be pets - each species should appear only once.

2. Use `COUNT` to see how many pets does 'Ron Weasley' own?

3. Can you have the output be 'Ron Weasley has 2 pets.'? (You need to concatenate strings)

4. Use `GROUP BY` to count how many pets each owner has. Give the output as 'NAME has X pets', with names alphabetically ordered (use `ORDER BY`).

5. Use `HAVING` to determine which owners only have one pet.

### 3. Build complex queries on multiple tables: JOINs

1. Use `JOIN`  to display the names of the pets and their Vertebrate Class.

2. Now let's find out what our pets look like: list all the pets, their apperance and their color.

3. Use `WHERE` to display the owners of male pets, the name of the pets and their vertebrate class.

4. Use `HAVING` to figure out which owner has pets of more than one vertebrate class.

5. Use `LEFT JOIN`. Compare the results for the following queries:

  ```SQL
  SELECT pets.name, animals.vertebrate_class
    FROM animals
    LEFT JOIN pets
    ON pets.species = animals.species;
  ```

  ```SQL
  SELECT pets.name, animals.vertebrate_class
    FROM pets
    LEFT JOIN animals
    ON pets.species = animals.species;
  ```

Despite the name of this section, the queries we are writing here remain quite simple. We will see during the program how to use different types of JOINs, subqueries and much more. Feel free to continue exploring the extra resources linked below.

_______________________________________
## Extra resources

Brushing up: These are referenced in the main resources section of the Chapter 3 `readme.md` and are repeated here for your convenience.
- [SQLZoo](http://sqlzoo.net/wiki/SQL_Tutorial) is a great online tutorial where you can try out your queries and is a great reference when you want to check basics 'how to'. Chapters 1 through 7 are particularly relevant for the precourse work.
- [Codacademy](https://www.codecademy.com/learn/learn-sql) has 4 chapters dedicated to SQL, in an interactive coding environment. You do not need to subscribe to the Pro Trial, the free material is already great if you want to practice basic SQL queries.

Extra information:
- a [visual explanation](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) of JOINs.
- a [comprehensive tutorial](https://www.tutorialspoint.com/sqlite/index.htm) on SQLite.
