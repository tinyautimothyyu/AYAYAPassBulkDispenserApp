import requests
import json

# Your API URL
url = "https://graph.facebook.com/v17.0/110567488787341/messages"

headers = {
    "Authorization": "Bearer EAAJXl7sAQcoBO40viApDACAYhBxjIZA90BK4lzPk2xYD6jnuwMgRnwVYM0ICJYpcSLFDh2haeGKg9ZC900Tau1OdX3MAs1sNKl9HijHnKw4X432bfoT9DoDUdQQqidXfZBbJiKokhlueK9pvksMHpYqYXRcZA1ZCvk7ZBiMDbZAsurAR1Vk27LZAVEsJN7oBPrMUH1qqOJvpzNfhCG3rZCz1iCidnvuSH8WDBT8xnXgZDZD",
    "Content-Type": "application/json"
}

# First you need to base64 encode your image
# Define the message content
body = { "messaging_product": "whatsapp", 
        "to": "16045377369", 
        "type": "image",
        "image": {
            "link": "https://drive.google.com/file/d/1QkxHNlDt3AyWKbnhb1dkw9jdI8kmPc1D/view?usp=sharing"
        }
        }

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(body))

# Print the response
if response.status_code == 200:
    print("Message sent successfully")
else:
    print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
