import boto3
import time

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-1",
            aws_access_key_id="AKIATAAUT7OL7M356SXL",
            aws_secret_access_key="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",
        )
        s3=boto3.client('s3')

    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3


s3 = s3_connection()

# # try:
# #     s3.upload_file('uploads\\pic.jpg',"ewha-2022-choi","test.jpg")
# # except Exception as e:
# #     print(e)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')

# Create the DynamoDB table.

print(time.asctime(time.localtime()))