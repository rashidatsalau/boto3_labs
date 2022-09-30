import boto3

ec2 = boto3.resource('ec2')
route_tables = ec2.route_tables.all()

for route_table in route_tables:
    for ra in route_table.routes_attribute:
        if ra.get('DestinationCidrBlock') == '0.0.0.0/0' and ra.get('GatewayId') is None:
            for rs in route_table.associations_attribute:
                if rs.get('SubnetId') is not None:
                    print(rs.get('SubnetId'))