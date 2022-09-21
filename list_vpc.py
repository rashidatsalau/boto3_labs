import boto3

session = boto3.Session(region_name='us-east-1')
ec2_resource = session.resource("ec2")
ec2_client = session.client("ec2")
subnet_ids = []
for vpc in ec2_resource.vpcs.all():
    # here you can choose which subnet based on the id
    if vpc.id == 'vpc-abcd1234':
        for subnet in vpc.subnets.all():
            subnet_ids.append(subnet.id)
# the result of this call has the data you're looking for
print(ec2_client.describe_subnets(SubnetIds=subnet_ids))