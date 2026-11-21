
import json

def lambda_handler(event, context):

    method = event.get("httpMethod", "GET")
    path = event.get("path", "/students")

    if method == "GET" and path == "/students":
        students = [
            {"id": 1, "name": "Malika", "course": "Data Science"},
            {"id": 2, "name": "Rahul", "course": "Computer Science"}
        ]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(students)
        }

    elif method == "POST" and path == "/students":
        body = event.get("body", "{}")
        student = json.loads(body)

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Student received successfully",
                "student": student
            })
        }

    return {
        "statusCode": 404,
        "body": json.dumps({"message": "Endpoint not found"})
    }


# Test 1: GET request
get_event = {
    "httpMethod": "GET",
    "path": "/students"
}

print("GET RESPONSE:")
print(lambda_handler(get_event, None))


# Test 2: POST request
post_event = {
    "httpMethod": "POST",
    "path": "/students",
    "body": json.dumps({
        "id": 3,
        "name": "Anu",
        "course": "Python"
    })
}

print("POST RESPONSE:")
print(lambda_handler(post_event, None))
