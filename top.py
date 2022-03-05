import boto3

client = boto3.client('s3')

response = client.list_buckets()
for b response ['Buckets']:
    print(b['Name']) 
