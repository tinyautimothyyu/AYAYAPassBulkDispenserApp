import requests
import json
import pandas as pd

class Media():
    def __init__(self):
        self.media_id = None

    def upload_media(self, PHONE_NUMBER_ID, ACCESS_TOKEN, file_path, type_="image/jpeg", messaging_product="whatsapp"):
        url = f'https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/media'

        headers = {
            'Authorization': 'Bearer ' + ACCESS_TOKEN,
        }

        file_name = file_path.split("/")[-1]
        
        files = {
            'file': (file_name, open(file_path, "rb"), type_),
            'type': (None, type_),
            'messaging_product': (None, messaging_product)
        }

        # Send the POST request
        response = requests.post(url, headers=headers, files=files)

        print(response.text)

        # Print the response
        if response.status_code == 200:
            print(f"Media {file_name} uploaded successfully")
            media_id = response.json().get('id')
            self.media_id = media_id
        else:
            print(f"Failed to upload media. Status code: {response.status_code}, Response: {response.text}")
        
        files["file"][1].close()

    def get_media_id(self):
        return self.media_id

class Contacts():
    def __init__(self, path):
        self.df = pd.read_csv(path, header=0)

    def get_phone_numbers(self):
        # Assuming phone numbers are stored in a column named 'phone_number'
        return self.df['Whatsapp #'].str.replace('-','').tolist()

class Messaging():
    def __init__(self, PHONE_NUMBER_ID, ACCESS_TOKEN):
        self.PHONE_NUMBER_ID = PHONE_NUMBER_ID
        self.ACCESS_TOKEN = ACCESS_TOKEN

    def _get_pass(self, PHONE_NUMBER):
        pass

    def send_announcement(self, PHONE_NUMBER, template="announcement_transition", language_code="zh_HK"):
        # API URL
        url = f"https://graph.facebook.com/v20.0/{self.PHONE_NUMBER_ID}/messages"

        # define headers
        headers = {
            "Authorization": "Bearer " + self.ACCESS_TOKEN,
            "Content-Type": "application/json"
        }

        if not PHONE_NUMBER:
            raise ValueError("Phone number is required for sending announcement")
        if not template:
            raise ValueError("Template name is required for sending announcement")
        if not language_code:
            raise ValueError("Language code is required for sending announcement")

        # define the body of the message
        body = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual", 
            "to": PHONE_NUMBER, 
            "type": "template",
            "template": {
                "name": template,
                "language": {"code": language_code}
            }
        }

        # Send the POST request
        response = requests.post(url, headers=headers, data=json.dumps(body))

        return response

    def send_message(self, PHONE_NUMBER, FILEPATH, FILENAME, template=False):

        # Path to the file
        FILEPATH += FILENAME

        # Your API URL
        url = f"https://graph.facebook.com/v20.0/{self.PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization": "Bearer " + self.ACCESS_TOKEN,
            "Content-Type": "application/json"
        }

        # get the file path of the AYAYA pass given the phone number
        # file = self._get_pass(PHONE_NUMBER)

        # instatiate the media object
        ayaya_pass = Media()
        
        # upload the document to WhatsApp media and obtain the media_id
        ayaya_pass.upload_media(self.PHONE_NUMBER_ID, self.ACCESS_TOKEN, FILEPATH)

        # get media_id
        media_id = ayaya_pass.get_media_id()

        if template:
            body = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual", 
                "to": PHONE_NUMBER, 
                "type": "template",
                "template": {
                    "name": "ayaya_pass",
                    "language": {"code": "en"},
                    "components": [
                        {
                            "type": "header",
                            "parameters": [
                                {
                                    "type": "image",
                                    "image": {
                                        "id": media_id
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        else:
        # Define the message content
            body = { "messaging_product": "whatsapp",
                    "recipient_type": "individual", 
                    "to": PHONE_NUMBER, 
                    "type": "image",
                    "image": {
                        "id": media_id
                    }
                    }

        # Send the POST request
        response = requests.post(url, headers=headers, data=json.dumps(body))

        # Print the response
        print(response.text)
        if response.status_code == 200:
            print(f"Message sent successfully to {PHONE_NUMBER}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")