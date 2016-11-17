# Outline

## The framework and storage of unprocessed data

**Hadoop**

* build hadoop framework

**S3**

* create enough buckets
* add correlative objects to buckets
* operate objects



## The ingestion and parsing for unprocessed data

**Apache Spark**

* read log file objects from data storage
* parse log file objects
* read other kinds of data objects from data storage
* format these data objects 
* return resulsts to data storage

**Amazon Kinesis streaming**

* read streaming data object from data storage
* parse streaming data object 
* return results to data storage



## The operation for formatted and cleaned data in data storage

**Hive**

* import formatted and cleaned data object to database
* export data from database to data storage

**Pig**

* write all kinds of scripts to operate data





