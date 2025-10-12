import boto3
import json 

def lambda_handler(event, context):
    client = boto3.client(service_name="bedrock-runtime")

    messages = [
        {"role": "user", "content": [{"text": "What is AWS?"}]},
    ]

    model_response = client.converse(
        modelId="us.amazon.nova-lite-v1:0", 
        messages=messages
    )
  
    return model_response["output"]["message"]["content"][0]["text"]
