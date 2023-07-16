import boto3


def all_users():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print('Username : {} Arn : {}'.format(username, Arn))


all_users()


##################################################################################

Username : aws-python Arn : arn:aws:iam::528418585832:user/aws-python
Username : itadmin-IAM Arn : arn:aws:iam::528418585832:user/itadmin-IAM
Username : testuser Arn : arn:aws:iam::528418585832:user/testuser
Username : testuser2 Arn : arn:aws:iam::528418585832:user/testuser2
Username : vprofile-s3-admin Arn : arn:aws:iam::528418585832:user/vprofile-s3-admin




#############################################

Some AWS operations return results that are incomplete and require subsequent requests in order to attain 
the entire result set. The process of sending subsequent requests to continue where a previous request left off is called pagination. 
For example, the list_objects operation of Amazon S3 returns up to 1000 objects at a time, and you must send subsequent requests with
the appropriate Marker in order to retrieve the next page of results.
