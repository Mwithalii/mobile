import tkinter as tk
import os
import africastalking
import dotenv
from dotenv import load_dotenv

load_dotenv()
api_key_path = os.getenv("API_KEY")


#initialize africastalking
africastalking.initialize(
    username='BADS',
    api_key=api_key_path
)

# Function to convert streak points into airtime
def convert_to_airtime():
    try:
        # Read streak points from the file
        with open('streak.txt', 'r') as file:
            streak_points = int(file.read())
        
        # Calculate the amount of airtime to redeem (e.g., 1 point = 1 KES)
        airtime_amount = streak_points  # Adjust this as needed
        
        # Use Africa's Talking API to send airtime to the user's phone number
        airtime = africastalking.Airtime
        response = airtime.send(phone_number, airtime_amount, "KES")
        
        if 'errorMessage' in response:
            result_label.config(text=f"Failed to send airtime: {response['errorMessage']}")
        else:
            result_label.config(text="Airtime sent successfully!")
    
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")

# Create the main tkinter window
root = tk.Tk()
root.title("Streaks to Airtime Converter")
root.geometry("400x200")

# Create a label to display instructions
instructions_label = tk.Label(root, text="Click 'Convert' to redeem your streak points for airtime.")
instructions_label.pack(pady=10)

# Create a button to initiate the conversion
convert_button = tk.Button(root, text="Convert", command=convert_to_airtime)
convert_button.pack(pady=10)

# Create a label to display the conversion result
result_label = tk.Label(root, text="")
result_label.pack()

# Phone number (replace with the user's phone number)
phone_number = "+254792281598"

root.mainloop()
