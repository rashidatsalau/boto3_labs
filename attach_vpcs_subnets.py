import boto3

client = boto3.client("ec2")
new_tag = [{'Key': 'Project', 'Value': 'Talent-Academy'}]
vpcs_response = client.describe_vpcs()
vpcs = vpcs_response['Vpcs']

vpc_ids = []
for vpc in vpcs:
    vpc_ids.append(vpc["VpcId"])
client.create_tags(Resources=vpc_ids, Tags=new_tag)

subnets_response = client.describe_subnets()
subnets = subnets_response['Subnets']

subnet_arn_list = []
for subnet in subnets:
    subnet_arn_list.append(subnet["SubnetArn"])


tagging_client = boto3.client('resourcegroupstaggingapi')
response = tagging_client.tag_resources(ResourceARNList=subnet_arn_list, Tags= {"Project": "Talent-Academy"})