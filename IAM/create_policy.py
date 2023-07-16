import boto3
import json


def create_policy():
    iam = boto3.client('iam')

    user_policy = {
        "Version":"2012-10-17",         # Administrative Access
        "Statement":[
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }


    response = iam.create_policy(
        PolicyName = 'pyFullAccess',
        PolicyDocument=json.dumps(user_policy)
    )

    print(response)


create_policy()

#########

{'Policy': {'PolicyName': 'pyFullAccess', 'PolicyId': 'ANPAXWCBTXTUBWXLIAJBC', 'Arn': 'arn:aws:iam::528418585832:policy/pyFullAccess', 
            'Path': '/', 'DefaultVersionId': 'v1', 'AttachmentCount': 0, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True, 
            'CreateDate': datetime.datetime(2023, 7, 16, 6, 38, 17, tzinfo=tzutc()), 'UpdateDate': datetime.datetime(2023, 7, 16, 6, 38, 17, 
            tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': '397f9404-d309-43f1-af63-6ee63b25a527', 'HTTPStatusCode': 200, 
                                                   'HTTPHeaders': {'x-amzn-requestid': '397f9404-d309-43f1-af63-6ee63b25a527', 
          'content-type': 'text/xml', 'content-length': '759', 'date': 'Sun, 16 Jul 2023 06:38:16 GMT'}, 'RetryAttempts': 0}}

Process finished with exit code 0
