import requests
import json
import pandas as pd

class Media():
    def __init__(self):
        self.media_id = None

    def upload_media(self, PHONE_NUMBER_ID, ACCESS_TOKEN, file, type_="application/pdf", messaging_product="whatsapp"):
        url = f'https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/media'

        headers = {
            'Authorization': 'Bearer ' + ACCESS_TOKEN,
        }

        body = {
            'file': file,
            'type': type_,
            'messaging_product': messaging_product
        }

        # Send the POST request
        response = requests.post(url, headers=headers, data=json.dumps(body))

        # Print the response
        if response.status_code == 200:
            print(f"Media {file} uploaded successfully")
            media_id = response.json().get('id')
            self.media_id = media_id
        else:
            print(f"Failed to upload media. Status code: {response.status_code}, Response: {response.text}")

    def get_media_id(self):
        return self.media_id

class Contacts():
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def get_phone_numbers(self):
        # Assuming phone numbers are stored in a column named 'phone_number'
        return self.df['phone_number'].tolist()

class Messaging():
    def __init__(self, PHONE_NUMBER_ID, ACCESS_TOKEN):
        self.PHONE_NUMBER_ID = PHONE_NUMBER_ID
        self.ACCESS_TOKEN = ACCESS_TOKEN

    def _get_pass(self, PHONE_NUMBER):
        pass

    def send_message(self, PHONE_NUMBER):

        # Your API URL
        url = f"https://graph.facebook.com/v17.0/{self.PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization": "Bearer " + self.ACCESS_TOKEN,
            "Content-Type": "application/json"
        }

        # get the file path of the AYAYA pass given the phone number
        file = self._get_pass(PHONE_NUMBER)

        # instatiate the media object
        ayaya_pass = Media()
        
        # upload the document to WhatsApp media and obtain the media_id
        ayaya_pass.upload_media(self.PHONE_NUMBER_ID, self.ACCESS_TOKEN, file)

        # get media_id
        media_id = ayaya_pass.get_media_id()

        # Define the message content
        body = { "messaging_product": "whatsapp",
                "recipient_type": "individual", 
                "to": PHONE_NUMBER, 
                "type": "document",
                "document": {
                    "id": media_id
                }
                }

        # Send the POST request
        response = requests.post(url, headers=headers, data=json.dumps(body))

        # Print the response
        if response.status_code == 200:
            print(f"Message sent successfully to {PHONE_NUMBER}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")