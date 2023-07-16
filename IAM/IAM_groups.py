## Create Group

import boto3


def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)


create_group('S3Admins')


## Attach Policy to group

import boto3


def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')

    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

    print(response)


attach_policy('arn:aws:iam::aws:policy/AmazonS3FullAccess','S3Admins')


## Adding user to IAM Group

import boto3


def add_user(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )

    print(response)

add_user('s3user', 'S3Admins')


## Detach Policy from user group

import boto3


def detach_group(user_group, arn):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn = arn
    )

    print(response)


detach_group('RDSAdmins', 'arn:aws:iam::aws:policy/AmazonRDSFullAccess')



## Create Access key for User

import boto3

'''
def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)



create_access('testuser')

'''


def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIAZPKDT2P2K2ESBO4H',
        Status='Inactive',
        UserName='testuser'

    )


update_access()


## Create Login

import boto3


def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        Password = 'Mypassword@1',
        PasswordResetRequired = False,
        UserName = username
    )

    print(login_profile)



create_login('test')


## Delete User

import boto3


def delete_myuser(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)



delete_myuser('testuser')


## Delete user from group

import boto3


def delete_user_group(username, groupName):
    iam = boto3.resource('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName=username
    )

    print(response)



delete_user_group('testuser', 'S3Admins')
