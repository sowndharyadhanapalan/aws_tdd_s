import os
import boto3
import json


class LambdaHandler:

    def __init__(self):
        self.lambdaclient = boto3.client('lambda')
        self.lambdaname = "start_glue_job"
        self.rolename = "arn:aws:iam::672580443112:role/trigger_lambda_glue"
        self.s3_session = boto3.session.Session()
        self.s3client = self.s3_session.client("s3")
        self.bucket = "test_bucket"
        self.file = "trigger_glue.zip"
        self.file_path = "C:\\Users\\s.b.dhanapalan\\Documents"

    def upload_file(self):
        path = os.path.join(self.file_path, self.file)
        self.s3client.upload_file(path, self.bucket, self.file)

    def create_lambda(self):

        create_lambda_function = self.lambdaclient.create_function(
            FunctionName=self.lambdaname,
            Runtime='python3.8',
            Role=self.rolename,
            Handler='{}.lambda_handler'.format('trigger_glue'),
            Description='trigger a glue job',
            Code={'S3Bucket': 'test_bucket', 'S3Key': 'trigger_glue.zip'}
        )

    def invoke_lambda(self):
        response = self.lambdaclient.invoke(
            FunctionName=self.lambdaname,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps({'job_name': "lambda_glue_s", 'detail': "lambda to glue trigger"})
        )
        return response


# lambda_client = boto3.client("lambda")
# lambdaevnt = LambdaHandler()
# lambdaevnt.create_lambda()
# lambdaevnt.invoke_lambda()