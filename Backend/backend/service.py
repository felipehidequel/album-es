import boto3
from botocore.exceptions import ClientError
from django.conf import settings

class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            aws_session_token=settings.AWS_SESSION_TOKEN,
            region_name=settings.AWS_S3_REGION_NAME
        )
        self.bucket = settings.AWS_STORAGE_BUCKET_NAME

    def create_folder(self, path):
        if not path.endswith('/'):
            path += '/'

        self.s3.put_object(Bucket=self.bucket, Key=path)

    def generate_presigned_url(self, key, expires_in=3600):
        return self.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket, 'Key': key},
            ExpiresIn=expires_in
        )