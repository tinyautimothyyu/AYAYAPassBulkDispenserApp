import requests
import json

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
            media_id = response.data.id  # assume the media_id is in data
            self.media_id = media_id
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

    def get_media_id(self):
        return self.media_id