 ## 1. Create EBS Volume

import boto3

'''
ec2_client = boto3.client('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone = 'us-east-1d',
    Size = 5,
    VolumeType='gp2',
    TagSpecifications = [
        {
            'ResourceType':'volume',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python & Boto3'
                }
            ]
        }
    ]
)

print("Created Volume ID : {} ".format(new_volume["VolumeId"]))

'''


ec2_client = boto3.resource('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone = 'us-east-1d',
    Size = 5,
    VolumeType='gp2',
    TagSpecifications = [
        {
            'ResourceType':'volume',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python & Boto3 with resource'
                }
            ]
        }
    ]
)

print("Created Volume ID : {} ".format(new_volume.id))


## 2. List Volumes

import boto3


ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.all():
    print(volume)


## 3. Search Volumes

import boto3

ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            'Name':'tag:Name',
            'Values': [
                'Python & Boto3',
            ]
        }
    ]
):
    print(f'Volume {volume.id} ({volume.size} Gib) -> {volume.state}')


## 4. Attach EBS to EC2

import boto3


ec2_resource = boto3.resource('ec2')

volume = ec2_resource.Volume('vol-0c65ed03ca559a04b')
print(f'Volume {volume.id} status -> {volume.state}')

volume.attach_to_instance(
    Device = '/dev/sdh',
    InstanceId='i-0e528c6f4a93c041d'
)

print(f'Volume {volume.id} Status -> {volume.state}')


## 5. Detach volume from EC2

import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

volume = ec2_resource.Volume('vol-0c65ed03ca559a04b')

volume.detach_from_instance(
    Device = '/dev/sdh',
    InstanceId='i-0e528c6f4a93c041d'
)

waiter = ec2_client.get_waiter('volume_available')
waiter.wait(
    VolumeIds=[
        volume.id
    ]
)

print(f'Volume {volume.id} Status -> {volume.state}')


## 6. Increase size of EBS volume

import boto3
ec2_client = boto3.client('ec2')
volume_id = 'vol-0c65ed03ca559a04b'

response = ec2_client.modify_volume(
    VolumeId=volume_id,
    Size=7
)

print(response)


## 7. Delete EBS Volume

import boto3

ec2_resource = boto3.resource('ec2')

volume = ec2_resource.Volume('vol-04a7e5595205649d8')

if volume.state == "available":
    volume.delete()
    print("Volume Deleted")
else:
    print("Can not delete volume attached")


## 8. Create EBS Snapshot

import boto3


ec2_resource = boto3.resource('ec2')
volume_id = 'vol-0d1a530e0b9563aca'

snapshot = ec2_resource.create_snapshot(
    VolumeId=volume_id,
    TagSpecifications = [
        {
            'ResourceType':'snapshot',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python Snapshot'
                }
            ]
        }
    ]
)

print('Snapshot is created')
