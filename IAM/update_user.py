import boto3


def update_user(old_username, new_username):
    iam = boto3.client('iam')

    response = iam.update_user(
        UserName=old_username,
        NewUserName=new_username   # update with new user name
    )

    print(response)


update_user('testuser2', 'testuser')


####
{'ResponseMetadata': {'RequestId': 'bd4d85fa-cb52-4653-9fdb-cb73865bde6e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'bd4d85fa-cb52-4653-9fdb-cb73865bde6e', 'content-type': 'text/xml', 'content-length': '200', 'date': 'Sun, 16 Jul 2023 06:30:12 GMT'}, 'RetryAttempts': 0}}
