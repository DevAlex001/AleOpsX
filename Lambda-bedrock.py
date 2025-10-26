import boto3
import json 

def lambda_handler(event, context):
    print(event.get("question"))
    question = event.get("question")
    client = boto3.client(service_name="bedrock-runtime")

    messages = [
        {"role": "user", "content": [{"text": f"{question}"}]},
    ]

    guardrail_config = {
        "guardrailIdentifier": "arn:aws:bedrock:us-east-2:340752832578:guardrail/l1cl9nocuzrk",
        "guardrailVersion": "1",
        "trace": "enabled",
    }

    model_response = client.converse(
        modelId="us.amazon.nova-lite-v1:0",
        messages=messages,
        guardrailConfig=guardrail_config
    )

    return model_response["output"]["message"]["content"][0]["text"]
