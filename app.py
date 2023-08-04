import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
phone_number_id = os.getenv('PHONE_NUMBER_ID')

if not access_token:
    raise ValueError("Access token not found. Please check your .env file.")
if not phone_number_id:
    raise ValueError("Phone number ID not found. Please check your .env file.")

def get_contacts_from_csv(path):
    df = pd.read_csv(path)
    pass

def get_pass(contact):
    pass

# Your API URL
url = f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"

headers = {
    "Authorization": "Bearer "+access_token,
    "Content-Type": "application/json"
}

def send_message(url, headers, contact_number, image_link):
    # First you need to base64 encode your image
    # Define the message content
    body = { "messaging_product": "whatsapp", 
            "to": contact_number, 
            "type": "image",
            "image": {
                "link": image_link
            }
            }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # Print the response
    if response.status_code == 200:
        print(f"Message sent successfully to {contact_number}")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
