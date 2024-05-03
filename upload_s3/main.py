import sys
import os
from dotenv import load_dotenv
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)
from upload_s3.upload_to_s3 import upload_file_to_s3

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get file path and bucket name from environment variables
    file_path = os.getenv("FILE_PATH")
    bucket_name = os.getenv("BUCKET_NAME")

    if file_path is None or bucket_name is None:
        print("Error: Please make sure FILE_PATH and BUCKET_NAME are set in the .env file.")
        return
    

    if upload_file_to_s3(file_path, bucket_name):
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")

if __name__ == "__main__":
    main()
