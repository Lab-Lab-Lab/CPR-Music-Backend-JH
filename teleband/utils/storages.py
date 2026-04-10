from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = None


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    default_acl = None
    file_overwrite = False
