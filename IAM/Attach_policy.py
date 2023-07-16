import boto3


def attach_policy(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

    print(response)


attach_policy('arn:aws:iam::aws:policy/AmazonRDSFullAccess', 'testuser')


###
{'ResponseMetadata': {'RequestId': '0767c989-12a9-4de3-bfd4-39b2c07bfbf8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '0767c989-12a9-4de3-bfd4-39b2c07bfbf8', 
'content-type': 'text/xml', 'content-length': '212', 'date': 'Sun, 16 Jul 2023 06:44:49 GMT'}, 'RetryAttempts': 0}}
