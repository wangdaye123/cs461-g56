# Cs461-g56

# Project: 
Prototype Big Data Archive in a Public Cloud

# Group member: 
Zhi Jiang</br>
Isaac T Chan</br>
Zhaoheng Wang

# Client:
David Barber
# Responsibility:
* Zhi Jiang: 
 * Load data from S3 into DynamoDB(Ingest and management of sample data)
 * Create table for DynamoDB
</br>
* Zhaoheng Wang:
 * Design the table for DynamoDB
 * Design the workflow for loading new data
 * Create visualization on QuickSight(Rudimentary analysis,visualization)
</br>
* Isaac T Chan:
 * Cost model for public cloud resources used
 * Test

# Environment:
The project is working on the Amazon Web services. So it requries to access to the AWS account.
    
# Instruction:
Instruction and Code can be found in Instruction and code folder

Load data from S3 into DynamoDB:
1. Start the instance on EC2 console
2. Open the terminal, find the primary key file(osu.pem) and connect to the EC2 instance find the primary key file and type ssh -i "osu.pem" ec2-user@ec2-35-164-136-118.us-west-2.compute.amazonaws.com
3. After connecting into the EC2 instance, run the python file create.py for creating table
4. After creating tables, run the address.py,data.py and onid.py for loading data
5. login in the DynamoDB and check the result on the console.
6. Stop the EC2 instance on EC2 console
</br>
Save the result back to the S3:
1. Open the DynamoDB console and choose the "DataForCapstone1" table.
2. Select the items in the table and Export to csv file
3. Open the S3 and click upload to upload the result 
</br>
Create visualization on the QuickSight
1. Open the QuickSight console on AWS 
2. Click New analysis button 
3. Choose New data set
4. Click upload a file and choose the csv file which export from the "DataForCapstone1" table
5. Using the data set and select the conlumn which need to evalaute.
6. Select the rows that need to evaluate and choose the visual types.
7. The visual will be created on right side.

# Introduction for project:
OSU campuses generate data constantly from multiples sources, including computer labs, wireless usage, student devices, and many others. This quantity of data, also known as big data, can effectively represent all kinds of behaviors of students for information technology. For example, analysis can be run to determine common student behaviors in order to allocate OSU resources more effectively. Currently, the data is very difficult to manage because it is collected from multiple sources and is impossible to analyze. The data is neither stored in the same formats nor in the same locations, meaning it is inaccessible and useful information is unable to be extracted.Our goal for this project is to unify and organize the data onto the consistent cloud platform of Amazon Web Services, which additionally provides utilities to manage and analyze. To achieve this, we plan to have a working prototype at the Engineering Expo that demonstrates the value of analyzing OSU big data and how the cost-to-value of our Amazon cloud solution compares to locally-hosted hardware. Our prototype will allow OSU big data to be analyzed and eventually it can be scaled to analyze all the data that OSU collects.
