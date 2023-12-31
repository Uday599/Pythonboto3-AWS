
## Docs Boto3 -> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

## 1. Describe EC2 Instance

import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

response = ec2_client.describe_instances()

pprint(response)


## 2. Create Key Pair

import boto3
from pprint import pprint


ec2_client = boto3.client('ec2')

resp = ec2_client.create_key_pair(
    KeyName = 'mykey',
    KeyType='rsa'
)

#pprint(resp['KeyMaterial'])

#store the pem file

file = open('mykey.pem', 'w')
file.write(resp['KeyMaterial'])
file.close()


## 3. Create Security Groups

import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description="This is desc",
    GroupName="pygroup",
    VpcId='vpc-027321ec9ba89707b'
)

print(response)

## 4. Creating Inbound Rule

import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.authorize_security_group_ingress(
    GroupId='sg-09b9ab986cbea7bcf',
    IpPermissions=[
        {
            'IpProtocol':'tcp',
            'FromPort':80,
            'ToPort':80,
            'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
        },
{
            'IpProtocol':'tcp',
            'FromPort':22,
            'ToPort':22,
            'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
        }
    ]
)

print(response)



## 5. Creating EC2 Instance

import boto3

ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instances(
    ImageId='ami-033b95fb8079dc481',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='mykey',
    SecurityGroups=[
        'pygroup'
    ]
)

print(response)


## 6. Get EC2 Public IP

import boto3


def get_ip(instance_id):
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))



get_ip('i-0cf2faaa79497a515')

## 7. List Running Instance

import boto3
def get_instances():
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances().get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            public_ip = instance['PublicIpAddress']
            private_ip = instance['PrivateIpAddress']

            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}"

get_instances()

## 8. Stop Instance

import boto3

def stope_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    print(response)

stope_instance('i-0cf2faaa79497a515')


## 9. Terminate Instance

import boto3


def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

terminate_instance('i-0cf2faaa79497a515')

## 10. Describe Security group

import boto3
from pprint import pprint


ec2_client = boto3.client('ec2')

response = ec2_client.describe_security_groups()
pprint(response)

## 11. Delete Security group

import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.delete_security_group(
    GroupId='sg-09b9ab986cbea7bcf'
)

print(response)

## 12. Delete Key Pair

import boto3


ec2_client = boto3.client('ec2')

response = ec2_client.delete_key_pair(
    KeyName='mykey'
)

print(response)


## 13. Attach User data 

import boto3


user_data_script = """
#!/bin/bash
yum update -y 
yum install -y httpd
chkconfig httpd on
service httpd start
echo "<h1>Welcome to Python & Boto3 Course</h1>" > /var/www/html/index.html

"""

ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instances(
    ImageId='ami-0b0dcb5067f052a63',
    MinCount= 1,
    MaxCount  =1,
    InstanceType='t2.micro',
    KeyName='mykey',
    SecurityGroups=[
        'launch-wizard-1'
    ],
    UserData = user_data_script
)

print(response)

