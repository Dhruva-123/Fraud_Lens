/*We create our Fraudlens database*/
CREATE DATABASE FraudLens;
USE FraudLens;

/*We create the table for our entire CSV. We write the exact same columns as that of the CSV to make the import as clean as possible*/
CREATE TABLE creditcard_transactions(
	TIME INT,
    V1 DOUBLE,
    V2 DOUBLE,
    V3 DOUBLE,
    V4 DOUBLE,
    V5 DOUBLE,
    V6 DOUBLE,
    V7 DOUBLE,
    V8 DOUBLE,
    V9 DOUBLE,
    V10 DOUBLE,
    V11 DOUBLE,
    V12 DOUBLE,
    V13 DOUBLE,
    V14 DOUBLE,
    V15 DOUBLE,
    V16 DOUBLE,
    V17 DOUBLE,
    V18 DOUBLE,
    V19 DOUBLE,
    V20 DOUBLE,
    V21 DOUBLE,
    V22 DOUBLE,
    V23 DOUBLE,
    V24 DOUBLE,
    V25 DOUBLE,
    V26 DOUBLE,
    V27 DOUBLE,
    V28 DOUBLE,
    Amount DOUBLE,
    Class VARCHAR(5)
);

/*The import is done via the terminal because the GUI method is far too slow. So there is no code for that here. However, I will explain the gist of it all.
First of all, we need to give ourself the permission to be able to read the csv into mysql. That is done via changing the SQL variables and restarting mysql. Once that is done, we can start the reading process.
Here is the code for it:

LOAD DATA LOCAL INFILE 'The_path_of_your_CSV'
INTO TABLE The_name_of_your_table
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

*/

/*Once that is done, we are checking the count of the import. Looks like we got all of the CSV.*/
USE fraudlens;
SELECT COUNT(*) FROM creditcard_transactions;


