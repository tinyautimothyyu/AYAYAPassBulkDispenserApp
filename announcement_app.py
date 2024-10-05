import argparse
from dotenv import load_dotenv
import os
from helpers import Contacts, Messaging

# Argument parsing
parser = argparse.ArgumentParser(description="Send AYAYA pass to contacts from a CSV file.")
parser.add_argument('-f', '--filename', type=str, help="Path to the CSV file containing contacts.")
args = parser.parse_args()
csv_path = args.filename

# Load environment variables
load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')

if not ACCESS_TOKEN:
    raise ValueError("Access token not found. Please check your .env file.")
if not PHONE_NUMBER_ID:
    raise ValueError("Phone number ID not found. Please check your .env file.")

# Create instances of Contacts and Messaging classes
contacts = Contacts(csv_path)
messaging = Messaging(PHONE_NUMBER_ID, ACCESS_TOKEN)

if not contacts:
    raise ValueError("No contacts found in the CSV file.")

# get the dataframe from Contacts 
data = contacts.df

# get the number of unique contacts from Contacts
unique_contacts = data['Whatsapp #'].nunique(dropna=True)

print(f"Received total of {data.shape[0]} contacts and {unique_contacts} unique contacts from the CSV file.\n")

numSuccess = 0

error = {}

# define phone number list
sent_phone_numbers = []

for index, row in data.iterrows():
    print('Sending AYAYA announcement to {} {}'.format(row['Given name'], row['Last name']))
    try:
        phone_number = row['Whatsapp #'].replace('-','')
        if phone_number not in sent_phone_numbers:
            response = messaging.send_announcement(phone_number)
            sent_phone_numbers.append(phone_number)

            # Print the response
            print(response.text)
            if response.status_code == 200:
                print(f"Message sent successfully to {phone_number}")
                numSuccess += 1
            else:
                error_msg = f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
                print(error_msg)
                error[f"{row['Given name']} {row['Last name']}"] = error_msg
        else:
            print(f"Message already sent to {phone_number}")
    except Exception as e:
        print(str(e))
        error[f"{row['Given name']} {row['Last name']}"] = str(e)
    print("\n")

print('Distribution of AYAYA announcement has completed...')
print(f'Recevied {data.shape[0]} total contacts and successfully sent announcement to {numSuccess}/{unique_contacts} of unique contacts.')
if error:
    for message in error:
        print(f"{message}: {error[message]}")
