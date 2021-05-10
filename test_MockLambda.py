from MockLambda import LambdaHandler
from MockS3 import S3Handler
import moto
import boto3
import docker


@moto.mock_lambda
@moto.mock_s3
def test_mocklambda():
    s3_client = boto3.resource("s3")
    s3_client.create_bucket(Bucket="test_bucket")
    s3evnt = S3Handler()
    s3evnt.upload_file()
    # lambda_client = boto3.client("lambda")
    lambdaevnt = LambdaHandler()
    lambdaevnt.create_lambda()
    response = lambdaevnt.invoke_lambda()
    print(response)


test_mocklambda()