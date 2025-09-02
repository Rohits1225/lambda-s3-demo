import boto3

# Create S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "rohit-my-s3-demo-bucket"  
    prefix = "test-folder/"                   # folder path (can be "" for root)

    try:
        # List objects in the bucket with the given prefix
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return {
                'statusCode': 200,
                'body': f"Files in {bucket_name}/{prefix}: {files}"
            }
        else:
            return {
                'statusCode': 200,
                'body': f"No files found in {bucket_name}/{prefix}"
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }

if __name__ == "__main__":
    response = lambda_handler({}, None)
    print(response)