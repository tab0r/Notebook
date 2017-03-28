# Chapter 3: SQL

### This is a review of how to write simple SQL queries, including the use of aggregates and of JOIN statements.
Structured Query Language (SQL) is used to interact with data stored in
relational databases.

There are many relational databases (PostgreSQL, MySQL, etc.) but they all share
SQL as a query language. In the program, we will be using PostgreSQL.

## Learning Objectives

- Install PostgreSQL (or default to SQLite).
- Connect to an SQL database via the command line.
- Create toy tables to test queries on.
- Write simple queries on a single table including SELECT, FROM, WHERE, CASE clauses and aggregates.
- Write queries based on standard use of JOIN statements.

## Main Resources

- [SQLZoo](http://sqlzoo.net/wiki/SQL_Tutorial) is a great online tutorial where you can try out your queries and is a great reference when you want to check basics 'how to'. Chapters 1 through 7 are particularly relevant for the precourse work.
- [Codacademy](https://www.codecademy.com/learn/learn-sql) has 4 chapters dedicated to SQL, in an interactive coding environment. You do not need to subscribe to the Pro Trial, the free material is already great if you want to practice basic SQL queries.
- [PostgreSQL Snippet](resources/create_sql_table.md) is a markdown file that walks you through how to create SQL tables in PostgreSQL.
- [Defaulting to SQLite](resources/defaulting_to_sqlite.md) is a markdown file that will help you to install SQLite and create SQL tables. Remember, only default to SQLite if you cannot get PostgreSQL up and running!

## Assignments

#### Instructions
In this chapter you will first install PostgreSQL and then be using SQL to answer the questions in 2 assignments by filling out [your_answers.txt](assignments/your_answers.txt).  Each answer should be the SQL query you wrote, and the result it returned.

### 0. Installation of PostgreSQL

[Assignment 0:](assignments/assignment_0_installation_psql.md) We will be working with PostgreSQL during the program. However, if you are unable to install it properly once you have gone through the steps in [assignment_0_installation_psql](assignments/assignment_0_installation_psql.md), you can turn to SQLite as it should be installed by default on your Mac. On other systems, we strongly recommend installing PostgreSQL.

If PostgreSQL was not successfully installed, you can find some information [here](resources/defaulting_to_sqlite.md) to help you with SQLite.

### 1. Simple tables: Pets in Harry Potter's world

[Assignment 1:](assignments/assignment_1_simple_tables.md) This first assignment is easier as it deals with a short database of pets in Harry Potter's World. Complete [assignment_1_simple_tables.md](assignments/assignment_1_simple_tables.md) to make sure you know how to write simple queries.

<b>* data to use:</b> You will be creating these SQL tables, but can use the `.csv` files in which the data is saved ([animals table](data/animals.csv) and [pets table](data/pets.csv)).

### 2. Real World Data: New York State's nursing home weekly bed census

[Assignment 2:](assignments/assignment_2_ny_state_data.md) This assignment is based on real data. You will be choosing one nursing home ("Facility") to focus on. Your queries will be for this subset of data only. Complete [assignment_2_ny_state_data.md](assignments/assignment_2_ny_state_data.md) and add your answers to the answer sheet.

<b>* data to use:</b>  The data comes from [nursing home weekly bed census](https://health.data.ny.gov/Health/Nursing-Home-Weekly-Bed-Census-Beginning-2009/uhyy-xp9s?), and has been converted to `.psql` format for your use. If you wish, you can explore other formats, notable `.sqlite` if you are using SQLite.

## Going Further: More resources

This section is only if you have time to spare and want to learn more about SQL.

- [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/). You can google around for comments on the exercises.
