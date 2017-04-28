import boto3

tname = 'table2'

# access DynamoDB
dynamodb = boto3.resource('dynamodb')
# access table
table = dynamodb.Table(tname)

# access S3
s3 = boto3.client('s3')
# access original file and download it
s3.download_file("isaac-data", "DataForCapStone.csv", "tmp.txt")

# import data from tmp.txt to table
f = open('tmp.txt')
num = 0
with table.batch_writer() as batch:
    for line in f:
        num += 1
        list_line = line.split(',')
        batch.put_item(
            Item = {
                'PIN': str((hash(list_line[1]+str(num)))),
                'ONID': list_line[1],
            }

        )
    f.close()