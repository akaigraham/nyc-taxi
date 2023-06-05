from time import sleep 
from prefect_aws import S3Bucket, AwsCredentials
import os

# create credentials block
def create_aws_creds_block():
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)
    
# create s3 bucket block 
def create_s3_bucket_block():
    aws_creds = AwsCredentials.load('my-aws-creds')
    my_s3_bucket_obj = S3Bucket(
        bucket_name='akg-prefect-bucket',
        credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="nyc-taxi-s3-bucket", overwrite=True)
    
if __name__ == '__main__':
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()