# Upload File to AWS S3

This project provides functionality to upload files to an Amazon Web Services (AWS) S3 bucket using Python script.

## Getting Started

To use this project, you'll need:

- Python installed on your local machine
- AWS account credentials with permissions to access the desired S3 bucket

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Farha-Dahman/Upload_to_S3.git
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Configure AWS credentials:
   - Setting environment variables:
     ```
     set AWS_ACCESS_KEY_ID=<your_access_key_id>
     set AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
     ```
   - Using the AWS CLI:
     ```
     aws configure
     ```
