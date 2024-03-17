import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)
from upload_s3.upload_to_s3 import upload_file_to_s3

def main():
    file_path = 'receipts\\receipt.txt'
    bucket_name = 'receipts-storage-pal'

    if upload_file_to_s3(file_path, bucket_name):
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")

if __name__ == "__main__":
    main()
