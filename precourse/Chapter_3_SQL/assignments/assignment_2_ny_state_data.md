# Assignment: New York State's nursing home weekly bed census

## Objectives

Write queries to interact with real data.

_______________________________________

## Questions & Answers

### Data
We will be using the `beds` data contained in the [data directory](../data/). This data comes from New York State's [nursing home weekly bed census](https://health.data.ny.gov/Health/Nursing-Home-Weekly-Bed-Census-Beginning-2009/uhyy-xp9s?) and is given to you in a few different formats.

* `beds.csv` is a comma-delimited file
* `beds.json` is JSON
* `beds.tsv` is tab-delimeted
* `beds.sql`is an SQL dump we will use with PostgreSQL.
* `beds.sqlite` is a SQLite3 database.

(Note that the first two of these came directly from the data portal, and we converted the CSV to the other formats.)

### Making the table

Just type in the terminal

```
$ psql -f beds.sql
```

### Answers
Please write your answers in [your_answers.txt](../assignments/your_answers.txt).

Note that you can find some basic SQL commands [here](../resources/basic_sql_commands.md), including how to upload the data and query it using SQL.

### Queries
Choose a nursing home ("Facility"), and subset the data by that nursing home.  Answer the following using SQL.

* The count of how many censuses were reported
* The earliest census date
* The latest census date
* The ten census dates with the highest number of available beds for that nursing home
* The ten census dates with the lowest number of available beds for that nursing home

_______________________________________
## Extra resources

- Handling dates can be tricky, investigate the `SUBSTRING` function in PostgreSQL.
