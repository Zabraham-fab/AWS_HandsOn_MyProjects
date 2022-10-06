import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Remove a new bucket
s3.delete(Bucket='xxxxxxx-boto3-bucket')

# Print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)