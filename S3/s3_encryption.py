 ## 1. Add Encryption

import boto3
def set_encryption():

    s3_client = boto3.client('s3')

    response = s3_client.put_bucket_encryption(
        Bucket="parwizforogh-12",
        ServerSideEncryptionConfiguration={
            "Rules":[
                {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm" : "AES256"}}
            ]
        }
    )

    print(response)
set_encryption()


## 2. Check Encryption

import boto3
from botocore.exceptions import ClientError


def check_encryption():
    s3_client = boto3.client('s3')

    try:
        response = s3_client.get_bucket_encryption(Bucket="parwizforogh-12")
        print(response)

    except ClientError as e:
        print("No encryption is available in this bucket")

check_encryption()



## 3. Add Policy to bucket

import boto3
import json

bucket_name = "parwizforogh-12"

bucket_policy = {
	"Version": "2012-10-17",
	"Id": "Policy1670146696267",
	"Statement": [
		{
			"Sid": "Stmt1670146603372",
			"Effect": "Deny",
			"Principal": "*",
			"Action": "s3:PutObject",
			"Resource": f'arn:aws:s3:::{bucket_name}/*',
			"Condition": {
				"StringNotEquals": {
					"s3:x-amz-server-side-encryption": "AES256"
				}
			}
		},
		{
			"Sid": "Stmt1670146692796",
			"Effect": "Deny",
			"Principal": "*",
			"Action": "s3:PutObject",
			"Resource": f'arn:aws:s3:::{bucket_name}/*',
			"Condition": {
				"Null": {
					"s3:x-amz-server-side-encryption": "true"
				}
			}
		}
	]
}

bucket_policy = json.dumps(bucket_policy)

s3_cleint = boto3.client('s3')
response = s3_cleint.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
print(response)


## 4. Get Bucket policy

import boto3

s3_client = boto3.client('s3')

response = s3_client.get_bucket_policy(Bucket='parwizforogh-12')
print(response['Policy'])


## 5. Delete Encryption 

import boto3
def delete_encryption():

    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket_encryption(Bucket='parwizforogh-12')
    print(response)
delete_encryption()
