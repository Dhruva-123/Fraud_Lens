
In order to import or load a csv into MySQL, we need to follow the following steps:

1. We need to create a table that we want to store the CSV in. Make sure that the table has the proper naming so that CSV can be imported.
2. We can use the 'Table Data Import Wizard' to do the import of a CSV into the MySQL table that we just created. Note that this can only be done for a dataset that is small. But the dataset we have here is exceptionally large (~200K rows). When I tried this approach, it took me nearly 15 mins to complete the import of ~700 rows. So this, clearly, is not an option for large datasets.
   
   So, the other option we have is to do it in SQL terminal. Here are the steps to do that:
	1. We need to have `infile` activated in MySQL workbench. But unfortunately, by default, it's turned off. So, we need to open the `my.init` file and add the line `local-infile=1` right under the `[mysqld]` title. Once that is done, we need to restart our workbench. 
	2. Then, we need to run this SQL commands in order to get our file imported:

```
LOAD DATA LOCAL INFILE 'Path_of_your_csv_file'
INTO TABLE name_of_your_table
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

What this does is, it locates the CSV file, it notes that each new line is a new row and each comma is a new column. It therefore gives us the proper table into the SQL table we already created. We want to `IGNORE 1 ROWS` because the first row for any CSV is the names of the columns. 

This is how we loaded the CSV into our SQL workbench.