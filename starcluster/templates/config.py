#!/usr/bin/env python
config_template = """
[section ec2]
#replace these with your AWS keys
AWS_ACCESS_KEY_ID = #your_aws_access_key_id
AWS_SECRET_ACCESS_KEY = #your_secret_access_key

# replace this with your account number
AWS_USERID= #your userid

# change this to your keypair location 
# (see the EC2 getting started guide tutorial on using ec2-add-keypair)
KEYNAME = #your keypair name
KEY_LOCATION = #/path/to/your/keypair

[section starcluster]
# ami for master
MASTER_IMAGE_ID = ami-00000000

# ami for nodes
IMAGE_ID = ami-11111111

# instance type
INSTANCE_TYPE = m1.small

# availability zone
AVAILABILITY_ZONE = us-east-1c

# attach volume to /home on master node
ATTACH_VOLUME = vol-abcdefgh
VOLUME_DEVICE = /dev/sdd
VOLUME_PARTITION = /dev/sdd1

# cluster size
DEFAULT_CLUSTER_SIZE = 2

# create the following user on the cluster
CLUSTER_USER = sgeadmin
"""
