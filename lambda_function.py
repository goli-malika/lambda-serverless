
def lambda_handler(event, context):

    name = event.get("name", "Guest")
    age = event.get("age", 0)

    message = f"Hello {name}! Your age is {age}."

    return {
        "statusCode": 200,
        "body": message
    }


# Test Case 1
event1 = {
    "name": "Malika",
    "age": 20
}

print(lambda_handler(event1, None))


# Test Case 2
event2 = {
    "name": "Rahul",
    "age": 22
}

print(lambda_handler(event2, None))


