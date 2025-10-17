import boto3
import json 

def lambda_handler(event, context):
    client = boto3.client(service_name="bedrock-runtime")

    messages = [
        {"role": "user", "content": [{"text": "What is automation?"}]},
    ]

    guardrail_config = {
        "guardrailIdentifier": "arn:aws:bedrock:us-east-2:340752832578:guardrail/ygjpsqisew0z",
        "guardrailVersion": "1",
        "trace": "enabled",
    }

    model_response = client.converse(
        modelId="us.amazon.nova-lite-v1:0",
        messages=messages,
        guardrailConfig=guardrail_config
    )

    return model_response["output"]["message"]["content"][0]["text"]
