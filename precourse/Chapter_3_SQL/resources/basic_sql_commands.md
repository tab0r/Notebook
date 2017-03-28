# SQL on real data

## Objective

These basic commands will walk you through accessing the data, looking at the tables, investigating their schema and writing simple queries.

## Basic commands

1. Loading the table in PostgreSQL

  ```
  $ psql -f beds.sql
  ```

2. Get the whole table. (This will take a while.)

  ```sql
  SELECT * FROM beds;
  ```

3. Get the first ten records.

  ```sql
  SELECT * FROM beds LIMIT 10;
  ```

4. Count how many records there are.

  ```sql
  SELECT count(*) FROM beds;
  ```

5. Count how many rows are XXX

  ```sql
  SELECT count(*) FROM beds WHERE Facility_ID = 28321;
  ```

6. Order

  ```sql
  SELECT * FROM beds ORDER BY Bed_Census_Date;
  ```

## Loading table for SQLite

These steps replace step 1 from the previous list:

a) To load the database, if you are in the same directory.

  ```sh
  $ sqlite3 beds.sqlite
  ```
  Otherwise, enter the filepath, for instance:
  ```sh
  sqlite3 data/beds.sqlite
  ```

b) Display headers

  ```
  >> .header on
  ```
c) A single SQLite3 database can contain many tables. List the tables.

```
>> .tables
```
d) Show a table schema

```
>> .schema beds
```
