import boto3

ec2_resource=boto3.resource("ec2")

instance = ec2.describe_instances(
    Filters=[{"Name": "tag:Name", "Values": ["your-instance-name"]}]

#Please select image id as per your EC2 instance requirement.
ec2_resource.create_instances(ImageId='ami-0cff7528ff583bf9a',
                          InstanceType='t2.micro',
                          MinCount=3,
                          MaxCount=3,
                          KeyName='my instance') #Enter your key name here
    
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))