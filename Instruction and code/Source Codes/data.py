import boto3

tname = "table1";

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tname)

s3 = boto3.client('s3')
s3.download_file("isaac-data", "DataForCapStone.csv", "tmp.txt")

f = open('tmp.txt')
num = 0
with table.batch_writer() as batch:
    for line in f:
        num += 1
        list_line = line.split(',') 
        batch.put_item(
            Item={
                'PIN': str(hash(list_line[1]+str(num))),
                'Company': list_line[11],  
                'ConnectTime': list_line[7],
                'DeviceLocation': list_line[5],
                'DeviceName': list_line[3],
                'DisconnectTime': list_line[6],
                'Manufacturer': list_line[17],
                'Model1': list_line[16],
                'Model2': list_line[18],
                'Num': int(list_line[10]),
                'OS': list_line[19],
                'OSDetail': list_line[20],
                'protocol': list_line[9],
                'Role': list_line[14],
                'Route': list_line[4],
                'Sp_wlan': list_line[12],
                'Sp_wlan2': list_line[13],
                'Timecost': list_line[8],
                'wireless_type': list_line[2],
            }        
        )
    f.close() 