import json

# Sample comment data
comments = [
    {
        "comment_id": 1,
        "user_id": 12345,
        "username": "user1",
        "content": "This video is awesome!",
        "likes": 100,
        "timestamp": "2023-06-01 10:30:00"
    },
    {
        "comment_id": 2,
        "user_id": 67890,
        "username": "user2",
        "content": "I love this video!",
        "likes": 50,
        "timestamp": "2023-06-01 12:15:00"
    },
    {
        "comment_id": 3,
        "user_id": 54321,
        "username": "user3",
        "content": "Great content!",
        "likes": 80,
        "timestamp": "2023-06-01 14:45:00"
    }
]

# Convert the data to JSON string
json_data = json.dumps(comments, indent=2)  # Use indent for pretty formatting (optional)

# Print or write the JSON data to a file
print(json_data)

# To write to a file, uncomment the following lines:
with open("comments.json", "w") as f:
    f.write(json_data)
