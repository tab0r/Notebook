# Defaulting to SQLite

## Learning Objectives

- Installing SQLite3.
- Creating SQL tables and inserting values.

You will be setting up SQLite only if your PostgreSQL installation was unsuccessful.

## Install SQLite

This will be very short set of instructions, as SQLite should already be installed on your Mac.

If you are running Mac or GNU/Linux, you probably already have `SQLite3` installed.
Try running it in the terminal.

```
sqlite3
```

If it's not installed, check your package manager, it might be called "sqlite" or "sqlite3".

If you're on Windows, download the Windows binaries from [here](http://www.sqlite.org/download.html).

More directions are [here](http://mislav.uniqpath.com/rails/install-sqlite3/).

## Creating tables and inserting values

There are a lot of similarities in the creation of tables in PostgreSQL and in SQLite. Some specific command will make using SQLite easier.

### Data of interest

Let's see different ways to create the following table, also available as `your_table.txt` ([click here for the file](your_table.txt)).

| column_1 | column_2 | column_3 |
| :------: | :------: | :------: |
| 1        | value_1  | value_a  |
| 2        | value_0  | value_a  |
| 3        | value_1  | value_b  |
| 4        | value_1  | value_c  |
| 5        | value_0  | value_a  |


### *Step 1:* Creating the database.

  ```
  $ sqlite3 <your_database.db>
  ```

### *Step 2:* Creating and populating the tables.

- Manual entry: The code is the same as for Postgres (note: restricting values would require a `check` which is outside the scope of this document).

  ```SQL
  -- Create <your_table> table --
  CREATE TABLE your_table(
    column_1 INT,
    column_2 TEXT,
    column_3 VARCHAR(10));
  ```

- Show table with the command `.tables`

- Automatic import: To create a table from a .csv file, just type

  ```SQL
  .mode csv your_table
  .import <path_to_the_csv_your_table.txt> your_table
  ```
Don't forget to use `pwd` to get the path to the file. You can interrogate the schema of the table used with `.schema your_table`.

- If you want to delete a table.

  ```SQL
  DROP TABLE IF EXISTS tablename;
  ```

- Check the content of your tables

  ```SQL
  SELECT * FROM your_table LIMIT 10;
  ```

Tip: when using sqlite, the results are easier to read with the following settings:

  ```SQL
  sqlite> .header on
  sqlite> .mode column
  ```
