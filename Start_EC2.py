import boto3
client = boto3.client('ec2')
resp=client.run_instances(ImageId='ami-0cff7528ff583bf9a',
        InstanceType='t2.micro',
        MinCount=3,
        MaxCount=3,
        KeyName= 'my instance',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Linux Server'},
                {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))