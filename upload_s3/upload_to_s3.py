import boto3
import os

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    # If S3 object_name is not specified use file name
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        response = s3_client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        return False
    
    return True
