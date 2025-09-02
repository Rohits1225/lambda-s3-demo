
# write into file present inside s3 bucket
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "rohit-my-s3-demo-bucket"
    file_key = "test-folder/hello.txt"
    file_content = "Hello, Rohit here try to overrite the content of existing file so now this is second file and this is my first file in S3!"

    s3.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)

    return {
        'statusCode': 200,
        'body': f"File '{file_key}' uploaded to S3 bucket '{bucket_name}'"
    }

if __name__ == "__main__":
    response = lambda_handler({}, None)
    print(response)
