import boto3

region = 'uap-southeast-2'

instances = ['i-03a5bb91ec9e697df']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))