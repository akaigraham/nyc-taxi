from time import sleep 
from prefect_aws import S3Bucket, AwsCredentials

# create credentials block
def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id='',
        aws_secret_access_key=''
    )