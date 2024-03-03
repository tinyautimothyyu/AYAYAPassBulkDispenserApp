import argparse
from dotenv import load_dotenv
import os
from helpers import Contacts, Messaging

# Argument parsing
parser = argparse.ArgumentParser(description="Send AYAYA pass to contacts from a CSV file.")
parser.add_argument('-f', '--filename', type=str, help="Path to the CSV file containing contacts.")
parser.add_argument('-d', '--directory', type=str, help="Path to the directory that contains AYAYA passes")
parser.add_argument('-t', '--template', action='store_true', help="Use WhatsApp template")
args = parser.parse_args()
csv_path = args.filename
passes_path = args.directory
use_template = args.template

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

print(f"Received {data.shape[0]} contacts from the CSV file.\n")

numSuccess = 0

error = {}

for index, row in data.iterrows():
    print('Sending AYAYA pass to {} {}'.format(row['Given name'], row['Last name']))
    try:
        phone_number = row['Whatsapp #'].replace('-','')
        filename = row['ID']+'.jpeg'
        messaging.send_message(phone_number, passes_path, filename, template=use_template)
        numSuccess += 1
    except Exception as e:
        print(str(e))
        error[f"{row['Given names']} {row['Last name']}"] = str(e)
    print("\n")

print('Distribution of AYAYA passes has completed...')
print(f'Recevied {data.shape[0]} and successfully sent passes to {numSuccess} contacts.')
if error:
    for message in error:
        print(f"{message}: {error[message]}")
