import datetime
import json
import random
import boto3
import time
from time import sleep

STREAM_NAME = "input-stream"


def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': random.randint(2,100)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partition1")


if __name__ == '__main__':
    sleep(1)
    generate(STREAM_NAME, boto3.client('kinesis', region_name='ap-south-1'))
