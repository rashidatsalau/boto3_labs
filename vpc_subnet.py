import boto3
client = boto3.client('ec2')

vpc = client.describe_vpcs()
subnets = client.describe_subnets()

mytags ={"Key": "Project", "Value": "Talent-Academy"}

for vpc_response in vpc["Vpcs"]:
    vpcid = vpc_response.get("VpcId", [])
    client.create_tags(
    Resources = [vpcid],
    Tags = [
        {
            "Key": "Project", 
            "Value": "Talent-Academy"
        },
    ]
)


for subnet_response in subnets['Subnets']:
    subnetid = subnet_response.get('SubnetId', [])
    client.create_tags(
    Resources = [subnetid],
    Tags = [
        {
            "Key": "Project", 
            "Value": "Talent-Academy"
        },
    ]
)






