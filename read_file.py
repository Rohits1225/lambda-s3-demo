# Reads (downloads) a file from an S3 bucket.
import boto3

# Create S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "rohit-my-s3-demo-bucket"   # bucket name
    file_key = "test-folder/hello.txt"        # file path in S3

    try:
        # Get the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)

        # Read file content
        file_content = response['Body'].read().decode('utf-8')
        print(file_content)

        return {
            'statusCode': 200,
            'body': f"Content of {file_key}: {file_content}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }

if __name__ == "__main__":
    response = lambda_handler({}, None)
    print(response)