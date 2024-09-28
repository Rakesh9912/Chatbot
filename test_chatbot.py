import requests

url = "http://127.0.0.1:5000/chat"
message = {"message": "What is your return policy?"}

response = requests.post(url, json=message)

# Check the status code and response text for debugging
print("Status Code:", response.status_code)
print("Response Text:", response.text)

if response.ok:
    print("Chatbot Response:", response.json())
else:
    print("Error:", response.status_code)
