# Instruction:
Instruction and Code can be found in Instruction and code folder

Load data from S3 into DynamoDB:
1. Go to AWS EC2 console and start `i-010e91199de2cf622` EC2 instance, then connect it
2. Open an SSH client. Locate your private key file ``osukeypair.pem``. Type command to connect this EC2 instance
3. After connecting into the EC2 instance, run the python file ``create.py`` for creating table
4. After creating tables, run the ``import.py`` for loading data
5. login in the DynamoDB and check the result on the console
6. Stop the EC2 instance on EC2 console

Save the result back to the S3:
1. anonymized record have been created after run the ``import.py``
2. It is stored in a certain bucket

Create visualization on the QuickSight
1. Open the QuickSight console on AWS 
2. Click New analysis button 
3. Choose New data set
4. Click upload a file and choose the csv file which export from the "DataForCapstone1" table
5. Using the data set and select the conlumn which need to evalaute.
6. Select the rows that need to evaluate and choose the visual types.
7. The visual will be created on right side.
