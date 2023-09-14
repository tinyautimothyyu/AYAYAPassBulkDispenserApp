import argparse
from dotenv import load_dotenv
import os
from helpers import Contacts, Messaging

# Argument parsing
parser = argparse.ArgumentParser(description="Send AYAYA pass to contacts from a CSV file.")
parser.add_argument('csv_path', type=str, help="Path to the CSV file containing contacts.")
parser.add_argument('passes_path', type=str, help="Path to the directory that contains AYAYA passes")
args = parser.parse_args()
csv_path = args.csv_path
passes_path = args.passes_path

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

for index, row in data.iterrows():
    phone_number = row['Whatsapp #'].replace('-','')
    filename = row['Filename']+'.jpeg'
    messaging.send_message(phone_number, passes_path, filename)
    
# phone_numbers = contacts.get_phone_numbers()

# for phone_number in phone_numbers:
#     messaging.send_message(phone_number)
