SET GLOBAL local_infile=TRUE;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Nutrition.csv'
INTO TABLE new_table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


CREATE TABLE `new_table2` (
  `YearStart` int NOT NULL,
  `YearEnd` int NOT NULL,
  `LocationAbbr` varchar(45) NOT NULL,
  `LocationDesc` varchar(45) NOT NULL,
  `Datasource` varchar(45) NOT NULL,
  `Class` varchar(45) NOT NULL,
  `Topic` varchar(45) NOT NULL,
  `Question` varchar(600) NOT NULL,
  `Data_Value_Unit` varchar(45) NOT NULL,
  `Data_Value_Type` varchar(45) NOT NULL,
  `Data_Value` double DEFAULT NULL,
  `Data_Value_Alt` double DEFAULT NULL,
  `Data_Value_Footnote_Symbol` varchar(45) NOT NULL,
  `Data_Value_Footnote` varchar(500) NOT NULL,
  `Low_Confidence_Limit` double DEFAULT NULL,
  `High_Confidence_Limit` double DEFAULT NULL,
  `Sample_Size` int NOT NULL,
  `Total` varchar(45) NOT NULL,
  `Age(years)` varchar(45) NOT NULL,
  `Education` varchar(45) NOT NULL,
  `Sex` varchar(45) NOT NULL,
  `Income` varchar(45) NOT NULL,
  `Race/Ethnicity` varchar(45) NOT NULL,
  `GeoLocation` varchar(45) NOT NULL,
  `ClassID` varchar(45) NOT NULL,
  `TopicID` varchar(45) NOT NULL,
  `QuestionID` varchar(45) NOT NULL,
  `DataValueTypeID` varchar(45) NOT NULL,
  `LocationID` int NOT NULL,
  `StratificationCategory1` varchar(45) NOT NULL,
  `Stratification1` varchar(45) NOT NULL,
  `StratificationCategoryId1` varchar(45) NOT NULL,
  `StratificationID1` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



SET GLOBAL local_infile=TRUE;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Nutrition.csv'
INTO TABLE new_table2
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
  @YearStart,
  @YearEnd,
  `LocationAbbr`,
  `LocationDesc`,
  `Datasource`,
  `Class`,
  `Topic`,
  `Question`,
  `Data_Value_Unit`,
  `Data_Value_Type`,
  @Data_Value,
  @Data_Value_Alt,
  `Data_Value_Footnote_Symbol`,
  `Data_Value_Footnote`,
  @Low_Confidence_Limit,
  @High_Confidence_Limit,
  @Sample_Size,
  `Total`,
  @Age_years,
  `Education`,
  `Sex`,
  `Income`,
  `Race/Ethnicity`,
  `GeoLocation`,
  `ClassID`,
  `TopicID`,
  `QuestionID`,
  `DataValueTypeID`,
  @LocationID,
  `StratificationCategory1`,
  `Stratification1`,
  `StratificationCategoryId1`,
  `StratificationID1`
)
SET
  `YearStart` = NULLIF(@YearStart, ''),
  `YearEnd` = NULLIF(@YearEnd, ''),
  `Data_Value` = NULLIF(@Data_Value, ''),
  `Data_Value_Alt` = NULLIF(@Data_Value_Alt, ''),
  `Low_Confidence_Limit` = NULLIF(@Low_Confidence_Limit, ''),
  `High_Confidence_Limit` = NULLIF(@High_Confidence_Limit, ''),
  `Sample_Size` = NULLIF(@Sample_Size, ''),
  `Age(years)` = NULLIF(@Age_years, ''),
  `LocationID` = NULLIF(@LocationID, '');



  SET GLOBAL local_infile=TRUE;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Nutrition.csv'
INTO TABLE new_table2
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
  @YearStart,
  @YearEnd,
  `LocationAbbr`,
  `LocationDesc`,
  `Datasource`,
  `Class`,
  `Topic`,
  `Question`,
  `Data_Value_Unit`,
  `Data_Value_Type`,
  @Data_Value,
  @Data_Value_Alt,
  `Data_Value_Footnote_Symbol`,
  `Data_Value_Footnote`,
  @Low_Confidence_Limit,
  @High_Confidence_Limit,
  @Sample_Size,
  `Total`,
  @Age_years,
  `Education`,
  `Sex`,
  `Income`,
  `Race/Ethnicity`,
  `GeoLocation`,
  `ClassID`,
  `TopicID`,
  `QuestionID`,
  `DataValueTypeID`,
  @LocationID,
  `StratificationCategory1`,
  `Stratification1`,
  `StratificationCategoryId1`,
  `StratificationID1`
)
SET
  `YearStart` = NULLIF(@YearStart, ''),
  `YearEnd` = NULLIF(@YearEnd, ''),
  `Data_Value` = NULLIF(@Data_Value, ''),
  `Data_Value_Alt` = NULLIF(@Data_Value_Alt, ''),
  `Low_Confidence_Limit` = NULLIF(@Low_Confidence_Limit, ''),
  `High_Confidence_Limit` = NULLIF(@High_Confidence_Limit, ''),
  `Sample_Size` = NULLIF(@Sample_Size, ''),
  `Age(years)` = NULLIF(@Age_years, ''),
  `LocationID` = NULLIF(@LocationID, '');


  CREATE TABLE `new_table2` (
  `YearStart` int NOT NULL,
  `YearEnd` int NOT NULL,
  `LocationAbbr` varchar(45) NOT NULL,
  `LocationDesc` varchar(45) NOT NULL,
  `Datasource` varchar(45) NOT NULL,
  `Class` varchar(45) NOT NULL,
  `Topic` varchar(45) NOT NULL,
  `Question` varchar(600) NOT NULL,
  `Data_Value_Unit` varchar(45) NOT NULL,
  `Data_Value_Type` varchar(45) NOT NULL,
  `Data_Value` double DEFAULT NULL,
  `Data_Value_Alt` double DEFAULT NULL,
  `Data_Value_Footnote_Symbol` varchar(45) NOT NULL,
  `Data_Value_Footnote` varchar(500) NOT NULL,
  `Low_Confidence_Limit` double DEFAULT NULL,
  `High_Confidence_Limit` double DEFAULT NULL,
  `Sample_Size` int DEFAULT NULL,
  `Total` varchar(45) NOT NULL,
  `Age(years)` varchar(45) DEFAULT NULL,
  `Education` varchar(45) NOT NULL,
  `Sex` varchar(45) NOT NULL,
  `Income` varchar(45) NOT NULL,
  `Race/Ethnicity` varchar(45) NOT NULL,
  `GeoLocation` varchar(45) NOT NULL,
  `ClassID` varchar(45) NOT NULL,
  `TopicID` varchar(45) NOT NULL,
  `QuestionID` varchar(45) NOT NULL,
  `DataValueTypeID` varchar(45) NOT NULL,
  `LocationID` int NOT NULL,
  `StratificationCategory1` varchar(45) NOT NULL,
  `Stratification1` varchar(45) NOT NULL,
  `StratificationCategoryId1` varchar(45) NOT NULL,
  `StratificationID1` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


SELECT * FROM new_table2
SELECT * FROM new_table2 WHERE Stratification1 = '$15,000 - $24,999'
SELECT * FROM new_table2 WHERE Stratification1 = '$15,000 - $24,999' AND Low_Confidence_Limit > 30
