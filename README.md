# CrimeInLA
Here I look into a public crime dataset on data.gov.

You can find the dataset here. I use the CSV version. 
https://catalog.data.gov/dataset/crime-data-from-2020-to-present

Here are some high level insights into the dataset before I go deeper.


<img width="1200" height="800" alt="Top10CrimeTypes" src="https://github.com/user-attachments/assets/5b507c5a-216b-44c9-9ab8-39495b2ce472" />

A decent amount of the crimes (above 100000) is related to car theft.

Here are also the top areas in LA and the number of crime entries per area.

<img width="1200" height="800" alt="Top15CrimeAreas" src="https://github.com/user-attachments/assets/f78dde30-43b3-421f-9750-25868234fb45" />

After grouping the dataset by month and ordering by month, we can see the number of crimes per month, assuming each data entry is an individual crime. There is a strange dropoff after 2024 that does not seem to be natural, but 2020 - 2024 can be assumed to be the legit trend.


<img width="1200" height="600" alt="EntriesPerMonth" src="https://github.com/user-attachments/assets/c647ffef-0604-4c23-afeb-6c6ea4d0fabd" />

Additionally it's interesting to note that crime tends to happen in the afternoon, and night more often than in the morning or noon.

<img width="1200" height="800" alt="CrimeByHour" src="https://github.com/user-attachments/assets/8da22995-27f9-4039-a32a-252dcdbc2cc2" />

# Nutrition and Obesity

Dataset is here: https://catalog.data.gov/dataset/nhis-adult-summary-health-statistics-b5ce9
Code is in analyze2.py

First I looked to try and find a relationship between income level and BMI. There were two metrics of BMI based on a confidence range. Low_Confidence_Limit is the low end of the range, and High_Confidence_Limit is the high end. I went with the low end of the range.

I was able to make a side by side boxplot of the BMIs, and its worth noting that high income (above 75000 USD) tends to have more variable BMI levels.
This makes sense if we consider that a higher income may allow someone to spend more money on food, and also that people with higher income may or may not be more aware of their diet.

<img width="800" height="600" alt="Nutrition_income" src="https://github.com/user-attachments/assets/6d323879-7209-4129-8ec7-a1fbee8cb127" />

I needed to remove NA values from this boxplot to make this possible.

## Practicing SQL and Database Management
To practice SQL, I downloaded mySQL workbench, mySQL Server, and mySQL. Setting up a server on Windows requires you to go to Services -> mySQL80 and then on mySQLWorkbench make a connection. I made a schema and a table, then imported the CSV through by running this code in SQL: 

`SET GLOBAL local_infile=TRUE;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Nutrition.csv'
INTO TABLE new_table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
`

Then I created a schema called Nutrition and a Table called my_table.

The database has a mix of INT, VARCHAR(45), VARCHAR(500), etc variables. Some variables that were supposed to be double are temporarily assigned as VARCHAR(45) due to some empty values which may have tabs or spaces in them.

## Challenges Overcome

There was an issue with the variables, such as Low_Confidence_Limit, which refused to be entered into the table as a double. I thought the error may have been with my code (SQL Code is above in query.sql) and it was, but it was not because of the NOT NULL constraints or the data in the dataset. It was because of the fact that the code expected the terminating character to be '\n' when it was '\r\n'.(https://stackoverflow.com/questions/33796151/mysql-error-1265-data-truncated-for-column-name-at-row)

So I fixed that, and I managed to enter the csv into mySQLWorkbench.

Additionally, it was a pain to define the table manually, as I was hoping Table Import Data Wizard would take care of it, but the program was far too slow at uploading.

Update: I realize the table was empty when I tried to fill it this way. I realize that the terminating character was actually '\n' all along. The issue is that when I did that, it gave an error saying Age(Years) or Sample_Size cannot be null. I simply allowed these columns to accept NULL and now the table is actualy filled.

Here is the output of mySQLWorkbench showing the successful run.

<img width="682" height="22" alt="mySQLOutput" src="https://github.com/user-attachments/assets/8befd0e1-702c-406f-ad75-de4a9dfdcdfc" />

## Querying

Some SQL Commands I tried are:

`SELECT * FROM new_table2`

This returned all 106260 rows.

`SELECT * FROM new_table2 WHERE Stratification1 = '$15,000 - $24,999'`

This returned 3795 rows. 

`SELECT * FROM new_table2 WHERE Stratification1 = '$15,000 - $24,999' AND Low_Confidence_Limit > 30`

This returned 1444 rows.

## BMI (Low) and Age

Here we can see the relationship between BMI (Low end of confidence range) and age, it tends to go up as people age.

<img width="800" height="600" alt="Nutrition_age" src="https://github.com/user-attachments/assets/9a59604b-4208-4782-9aaa-f162c8bf40c5" />

## Power BI

Here I try using PowerBI to get the average percentage of people, who fit a specific description, by group.
Right here i filter out weird percentage values above 100:
<img width="955" height="144" alt="filter" src="https://github.com/user-attachments/assets/5e64419d-37ca-47e7-84b8-84333b5f3cc4" />

And here is a dashboard with multiple bar charts for each decription, of the average percentage of people that fit that description, by group.

<img width="1385" height="593" alt="dashboard1" src="https://github.com/user-attachments/assets/e0caf0fa-b571-4d6f-b543-6b7877bf52c6" />




