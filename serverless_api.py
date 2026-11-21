
import json

def lambda_handler(event, context):

    method = event.get("httpMethod", "GET")

    if method == "GET":
        response = {
            "message": "Welcome to Malika's Serverless API!",
            "service": "AWS Lambda",
            "status": "Success"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response)
        }

    return {
        "statusCode": 405,
        "body": json.dumps({"message": "Method Not Allowed"})
    }


# Simulated API Gateway request
test_event = {
    "httpMethod": "GET"
}

result = lambda_handler(test_event, None)

print(result)
