import boto3
import sys
import csv
import os
from boto3.dynamodb.conditions import Attr
from datetime import datetime

# set bucket and file
input_bucket = str(sys.argv[1])
file_name = str(sys.argv[2])
output_bucket = str(sys.argv[3])

# set name to tables
tname1 = 'ONID'
tname2 = 'Mac_Address'
tname3 = 'Records'

# access DynamoDB
dynamodb = boto3.resource('dynamodb')

# access table
ONID = dynamodb.Table(tname1)
Mac_Address = dynamodb.Table(tname2)
Records = dynamodb.Table(tname3)

# access S3
s3 = boto3.client('s3')

# access original file and download it
s3.download_file(input_bucket, file_name, "tmp.txt")

# open the temporary file
f = open('tmp.txt')
num = 0

# read the file line by line
for line in f:
    num += 1
    
    list_line = line.split(',')
    
    # avoid empty value
    for i in range(len(list_line)):
        if list_line[i] == '':
            list_line[i] = "empty"

    check_mac = list_line[0]
    check_onid = list_line[1]
    
    # check MAC address
    response = Mac_Address.scan(
        FilterExpression = Attr('Address').contains(check_mac)
    )
    count1 = response['Count']

    # check ONID
    response2 = ONID.scan(
        FilterExpression = Attr('ONID').contains(check_onid)
    )
    count2 = response['Count']

    # If is a new ONID/MAC
    if count1 == 0 and count2 == 0:
        # create a new PIN
        PIN = str(hash(check_onid + check_mac + str(num)))
    
        Mac_Address.put_item(
            Item = {
                'PIN': PIN,
                'Address': list_line[0],
            }

        )

        ONID.put_item(
            Item = {
                'PIN': PIN,
                'ONID': list_line[1],
            }
        )
    
        Records.put_item(
            Item={
                'PIN': PIN,
                'OSU_Role': list_line[2],
                'Device_Name': list_line[3],
                'Device_Location': list_line[4],
                'Connect_Time': list_line[5],
                'Disconnect_Time': list_line[6],
                'Total_Traffic': list_line[8],
                'Avg_Usage': list_line[9],
                'AP_Radio': list_line[10],
                'Connection_Mode': list_line[11],
                'Device_Type': list_line[12],
                'Manufacturer': list_line[13],
                'Model': list_line[14],
                'OS': list_line[15],
                'OS_Detail': list_line[16],
            }
        )
    # We need to update this item
    else:
        # If it is not new ONID/MAC
        Records.update_item(
            Key={
                'PIN': str(hash(check_onid + check_mac + str(num))),
            },
            UpdateExpression='SET OSU_Role = :role, Device_Name = :d_name, Device_Location = :d_location, Connect_Time = :c_time, Disconnect_Time = :d_time, Total_Traffic = :t_t, Avg_Usage = :a_u, AP_Radio = :a_r, Connection_Mode = :c_mode, Device_Type = :d_t, Manufacturer = :man, Model = :model, OS = :os, OS_Detail = :os_d',
            ExpressionAttributeValues={
                ':role': list_line[2],
                ':d_name': list_line[3],
                ':d_location': list_line[4],
                ':c_time': list_line[5],
                ':d_time': list_line[6],
                ':t_t': list_line[8],
                ':a_u': list_line[9],
                ':a_r': list_line[10],
                ':c_mode': list_line[11],
                ':d_t': list_line[12],
                ':man': list_line[13],
                ':model': list_line[14],
                ':os': list_line[15],
                ':os_d': list_line[16],
            }
        )
f.close

# set name to file of anonymized record
file_name = str(datetime.now()) + str('.csv')

# access Records table
response = Records.scan()

# write data to file of anoymized record
with open(file_name, 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for i in response['Items']:
        writer.writerow([i['PIN'], i['AP_Radio'], i['Avg_Usage'], i['Connect_Time'], i['Connection_Mode'],  i['Disconnect_Time'], i['Device_Location'], i['Device_Type'], i['Device_Name'], i['Manufacturer'], i['Model'], i['OS'], i['OS_Detail'], i['OSU_Role'], i['Total_Traffic']])

# upload file of anonymized record to S3
s3.upload_file(file_name, output_bucket, file_name)

os.remove(file_name)
os.remove('tmp.txt')
