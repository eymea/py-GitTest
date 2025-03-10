import json
import sys

def lambda_handler(event, context):
    # TODO implement

    print(sys.version)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! V3')
    }

if __name__ == "__main__":
    print(lambda_handler({}, {}))