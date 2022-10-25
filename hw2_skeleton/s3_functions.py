import boto3
import time


#s3 연결
s3= boto3.client('s3')

#dynamodb의 table 연결
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')

def upload_post(file_name, title, text, BUCKET, TABLE):
    #file형태로 upload한 사진 s3에 저장
    try:
        s3.upload_file(file_name,BUCKET,file_name)
    except Exception as e:
        print(e)
    #dynamodb에 file_name, title, text, BUCKET, TABLE 애트리뷰트 값 넣기
    table.put_item(
        Item={
            'TABLE': TABLE ,
            'file_name': file_name ,
            'title': title ,
            'text': text ,
            'BUCKET': BUCKET
        }
    )

def get_url(file_name, BUCKET):
    url=f'https://{BUCKET}.s3.ap-northeast-1.amazonaws.com/{file_name}'     
    return url

now = time.localtime()

#dynanodb에 있는 table item 조회
def get_items(TABLE):
    response = table.get_item(
        Key ={
            'TABLE': TABLE
        }
    )   
    item = response['Item']

    dates = [time.strftime('%c',now)]
    
    titles = [item['title']]

    urls = [get_url(item['file_name'], item['BUCKET'])]

    texts = [(item['text'])]

    return dates, titles, urls, texts


def delete_post(key, BUCKET, TABLE):
    table.delete_item(
        key={
            'TABLE': TABLE
        }
    )
