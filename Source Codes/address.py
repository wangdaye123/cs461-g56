import boto3

tname = 'table3'

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
            Item = {
                'PIN': str((hash(list_line[1]+str(num)))),
                'Address': list_line[0],
            }

        )
    f.close()