# Create your SQL tables

## Learning Objectives

- Learn how to create a table.
- Learn how to insert values in that table (two methods: `INSERT` or `COPY`).

You will have some code that you can re-use to create your own tables during the program.

NB: this is a PostgreSQL (psql) version, click [here](defaulting_to_sqlite.md) for SQLite.

## Steps in a table creation

### Brief Overview

1. Create a psql database.
2. Create psql tables.
3. Insert values manually.
4. Insert values from a file.

### Data of interest

Let's see different ways to create the following table, also available as `your_table.txt` ([click here for the file](your_table.txt)).

| column_1 | column_2 | column_3 |
| :------: | :------: | :------: |
| 1        | value_1  | value_a  |
| 2        | value_0  | value_a  |
| 3        | value_1  | value_b  |
| 4        | value_1  | value_c  |
| 5        | value_0  | value_a  |

### *Step 1:* Creating your database.

1. Open PostgreSQL (from the command line or from the application you installed, with a cute elephant icon).
2. You are now in the `psql`command line interface. This is what it will typically look like.

  ```
  [user@ directory]$ psql
  psql (9.4.4)
  Type "help" for help.

  user=#
  ```
3. You can list databases with the command `\l` or `\list`.
4. Create your own database (name in lowercase letters) and check it was created.

  ```SQL
  -- Create a Database --
  CREATE DATABASE <your_database>;
  ```

5. To get out of `psql`, type `\q`.

You can skip this step and create your tables in a public database. Please note it is not good practice.

### *Step 2:* Creating your tables.

1. Let's enter our database to create SQL tables.
  ```
  $ psql <your_database>
  ```
The prompt will now read `<your_database>=#`.

2. You can create a new table by specifying the table name, along with all column names and their types.

  ```SQL
  -- Create <your_table> table --
  CREATE TABLE your_table(
    column_1 INT,
    column_2 TEXT,
    column_3 VARCHAR(10));
  ```
  - Sometimes you know in advance the list of values a given column can contain. In that case you can restrict accessible values for that column.

  ```SQL
  -- Restrict the possible values for a column --
  CREATE TYPE column_3_type AS ENUM ('value_a', 'value_b', 'value_c');
  CREATE TYPE column_2_type AS ENUM ('value_0', 'value_1');

  -- Create <your_table> table --
  CREATE TABLE your_table(
    column_1 INT,
    column_2 column_2_type,
    column_3 column_3_type);
  ```

3. Show tables with the command `\dt`.

4. Drop a table.

  ```SQL
  DROP TABLE your_table;
  ```

### *Step 3_1:* Insert values in the table manually.

- Insert values by hand with the scheme `INSERT INTO tablename VALUES (x,y,z);`.

  ```SQL
  INSERT INTO your_table VALUES (1, value_1, value_a);
  INSERT INTO your_table VALUES (2, value_0, value_a);
  INSERT INTO your_table VALUES (3, value_1, value_b);
  INSERT INTO your_table VALUES (4, value_1, value_c);
  INSERT INTO your_table VALUES (5, value_0, value_a);
  ```
This approach can quickly become tedious.

### *Step 3_2:* Insert values in the table from a file.

- Insert values from a file (here a `.txt` or `.csv` with a first line as a header).

  ```SQL
  COPY your_table FROM <path_to_the_csv_your_table.txt> DELIMITER ',' CSV HEADER
  ```

  Remember the `pwd` command to get the path to the file. If the line above does not work, try using `\COPY`.

  ```SQL
  \COPY your_table FROM <path_to_the_csv_your_table.txt> DELIMITER ',' CSV HEADER
  ```

### Checking your work.

- Check the content of your tables

  ```SQL
  SELECT * FROM your_table LIMIT 10;
  ```
