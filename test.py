import africastalking
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()
username = 'BADS'
api_key= os.getenv("API_KEY")

print(f"Username: {username}")
print(f"API Key: {api_key}")


""" #initialize africastalking
africastalking.initialize(
    username=username_path,
    api_key=api_key_path
)

sms = africastalking.SMS

username = "Dennis"
hone= "+254792281598"
message = f"Hello {username}, your account has been created successfully!"
response = sms.send(message, [hone])
print(response) """