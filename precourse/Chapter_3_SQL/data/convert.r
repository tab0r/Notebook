#!/usr/bin/env Rscript

# This is the code we used to convert the original CSV
# file into TSV and SQlite3.

# Read
beds <- read.csv('beds.csv', stringsAsFactors = F)

# SQLite
library(RSQLite)
con <- dbConnect(dbDriver("SQLite"), dbname = 'beds.sqlite')
dbWriteTable(con, "beds", beds, row.names = F, overwrite = T)
dbDisconnect(con)

# TSV
write.table(beds, file = 'beds.tsv', sep = '\t', row.names = F)
