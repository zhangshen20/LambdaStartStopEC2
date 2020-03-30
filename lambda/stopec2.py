import boto3

region = 'ap-southeast-2'

instances = ['i-03a5bb91ec9e697df']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))