# Spark_and_data_lakes_with_AWS_Glue
Project successfully completed as part of the Udacity data engineering nanodegree. This project is done using AWS as cloud infrastructure and some of it services like S3, Glue and Athena. In order to access the project data, you can use this [link](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter).

# Problem statement
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

- Trains the user to do a STEDI balance exercise
- Has sensors on the device that collect data to train a machine-learning algorithm to detect steps
- Has a companion mobile app that collects customer data and interacts with the device sensors

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## Prompt
As a data engineer on the STEDI Step Trainer team, extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS. The intent is for the company's Data Scientists to use the solution to train machine learning models.

## The Device
There are sensors on the device that collect data to train a machine learning algorithm to detect steps. It also has a companion mobile app that collects customer data and interacts with the device sensors. The step trainer is just a motion sensor that records the distance of the object detected.

## The Data

1. Customer Records:

Contains the following fields:
  serialnumber
  sharewithpublicasofdate
  birthday
  registrationdate
  sharewithresearchasofdate
  customername
  email
  lastupdatedate
  phone
  sharewithfriendsasofdate

2. Step Trainer Records (data from the motion sensor):

Contains the following fields:
  sensorReadingTime
  serialNumber
  distanceFromObject

3. Accelerometer Records (from the mobile app):

Contains the following fields:
  timeStamp
  user
  x
  y
  z

# Usage

## Prerequisites
- An S3 bucket to store data categorized into either the landing, trusted, or curated zone
- Landing zone S3 buckets to ingest raw customer, step trainer, and accelerometer JSON files
- IAM permissions for S3, Glue, and Athena
- Database specific for project's Glue tables, e.g. project

## Outline
The solution is built on AWS and uses the following services:

- S3 for data storage
- Glue for data processing
- Athena for querying data
  
My data lakehouse solution is comprised of five Python scripts which are run in AWS Glue. The scripts are run in the following order:

1. `customer_landing_to_trusted.py`: This script transfers customer data from the 'landing' to 'trusted' zones. It filters for customers who have agreed to share data with researchers.

2. `accelerometer_landing_to_trusted.py`: This script transfers accelerometer data from the 'landing' to 'trusted' zones. It filters for Accelerometer readings from customers who have agreed to share data with researchers.

3. `customer_trusted_to_curated.py`: This script transfers customer data from the 'trusted' to 'curated' zones. It filters for customers with Accelerometer readings and have agreed to share data with researchers.

4. `step_trainer_Landing_to_Curated.py`: This script transfers step trainer data from the 'landing' to 'curated' zones. It filters for curated customers with Step Trainer readings.

5. `machine_learning_curated.py`: This script combines Step Trainer and Accelerometer data from the 'curated' zone into a single table to train a machine learning model.

## Directions

To create Customer Landing Zone
a. Run `customer_landing.sql` script in Athena to create customer_landing table

To create Accelerometer Landing Zone
b. Run `accelerometer_landing.sql` script in Athena to create accelerometer_landing table

To create Step Trainer Landing Zone
c. Run `step_trainer_landing.sql` script in Athena to create step_trainer_landing table

To create Customer Trusted Zone
Run `customer_landing_to_trusted.py` script in Glue to create customer_trusted table

To create Accelerometer Trusted Zone
Run `accelerometer_landing_to_trusted.py` script in Glue to create accelerometer_trusted table

To create Customer Curated Zone
Run `customer_trusted_to_curated.py` script in Glue to create customer_curated table

To create Step Trainer Curated Zone
Run `step_trainer_landing_to_curated.py` script in Glue to create step_trainer_curated table

To create Machine Learning Curated Zone
Run `machine_learning_curated.py` script in Glue to create machine_learning_curated table

# Solution
## Technical discussion

In a data lake architecture, the use of landing, trusted, and curated zones serves specific purposes that can significantly enhance the quality, reliability, and usability.

Landing Zone: The landing zone is often the first point of contact for raw data as it enters the data lake. It serves as a staging area where data from various sources is collected, often in its original format. This zone provides a place to accumulate data before any substantial processing occurs. This allows for flexibility, as the original raw data remains intact and available for different types of analysis or processing in the future.

Trusted Zone: After data has been landed, it may then be processed and moved to the trusted zone. In this zone, data is cleansed, validated, and often transformed into a structured format. This can include operations like deduplication, handling missing or incorrect data, and ensuring our customers have approved their data to be used for research purposes. The trusted zone is designed to be a source of reliable data for further analysis.

Curated Zone: The curated zone is where data is further transformed, often to meet the specific needs of a particular analysis, application, or group of users. This may involve operations like aggregating data, creating derived metrics, or combining multiple datasets. The curated zone should provide data that's ready-to-use for your specific data-driven applications and analyses.

In essence, these three zones facilitate a layered approach to data management and preparation. Each stage adds value to the data, making it increasingly reliable and useful for our specific needs. This strategy also aids in maintaining data quality, tracking data lineage, and enabling efficient and versatile data exploration and analysis.

## Business discussion

Our data lakehouse solution is designed to give STEDI a robust and flexible data infrastructure that allows us to store, clean, and transform vast amounts of data.

Firstly, my solution provides scalability and cost efficiency by leveraging Amazon S3 for storage, enabling us to store large amounts of diverse data cost-effectively. We can scale our storage up or down based on our needs, and we only pay for what we use.

Secondly, by using AWS Glue, a fully managed extract, transform, and load (ETL) service, we are able to clean, normalize, and relocate our data. This step is crucial for preparing our data for high-quality analytics and machine learning.

The structured data is then ready for downstream use by our data scientists for exploratory data analysis or to train machine learning models.

Moreover, my solution provides a single source of truth for our data, improving data quality and consistency. This is particularly beneficial when dealing with complex datasets as it simplifies the process of data management and increases efficiency.

Overall, my data lakehouse solution gives us the power to make data-driven decisions, enhancing STEDI's competitive advantage in the market, improving our products, and delivering a superior customer experience.
