from tkinter import *
import africastalking
import dotenv
from dotenv import load_dotenv
import os
from tkinter import messagebox
from tkinter import simpledialog

load_dotenv()
api_key_path = os.getenv("API_KEY")

def get_recipient_phone_number():
    try:
        with open('datasheet.txt', 'r') as file:
            data = file.read()
            data_dict = eval(data)
            return data_dict.get('phone', None)
    except Exception as e:
        print(f"Error reading datasheet.txt: {str(e)}")
        return None

def read_streaks_from_file():
    try:
        with open('streak.txt', 'r+') as file:
            streaks = int(file.readline())
            return streaks
    except FileNotFoundError:
        return None

def update_streaks_file(new_streaks):
    try:
        with open('streak.txt', 'w') as file:
            file.write(str(new_streaks))
    except Exception as e:
        print(f"Error updating streaks in streak.txt: {str(e)}")

def convert_points_or_amount(value, from_unit, to_unit):
    # Set the conversion rates (1 point = 1 dollars)
    # Set the conversion rates (1 point = 1 ksh)
    point_to_amount_rate = 1
    amount_to_point_rate = 1

    # Initialize the result variable
    result = None

    # Check the input units and perform the appropriate conversion
    if from_unit == 'points' and to_unit == 'amount':
        result = value * point_to_amount_rate
    elif from_unit == 'amount' and to_unit == 'points':
        result = value * amount_to_point_rate
    else:
        # If the units are invalid or the input value is not a number, return an error dictionary
        return {
            'status': False,
            'statusCode': 400,
            'message': 'Units are invalid or the input value is not a number'
        }

    # Return the result rounded to two decimal places
    return round(result, 2)

def convert_and_display(points_to_convert):
    if points_to_convert is not None:
        result = convert_points_or_amount(points_to_convert, 'points', 'amount')
        messagebox.showinfo("Conversion Result", f"{points_to_convert} points is equivalent to KES {result:.2f}")
        return result
    else:
        messagebox.showerror("File Not Found", "The 'streak.txt' file was not found.")

class AIRTIME:
    def __init__(self):
        # Set your app credentials
        self.username = "BADS"
        self.api_key = api_key_path

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the airtime service
        self.airtime = africastalking.Airtime

    def send(self, amount):
        # Set phone_number in international format
        phone_number = get_recipient_phone_number()

        # Set The 3-Letter ISO currency code
        currency_code = "KES"

        try:
            # That's it, hit send and we'll take care of the rest
            responses = self.airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
            print(responses)
        except Exception as e:
            print("Encountered an error while sending airtime: %s" % str(e))

if __name__ == '__main__':
    streaks = read_streaks_from_file()
    if streaks is not None:
        points_to_convert_str = simpledialog.askstring("Input", "1point = KES 1.00 \n Enter the number of points to convert:")
        if points_to_convert_str:
            points_to_convert = int(points_to_convert_str)
            if points_to_convert >= 10 and points_to_convert <= streaks:
                new_streaks = streaks - points_to_convert  # Subtract points from streaks
                update_streaks_file(new_streaks)  # Update streaks in the file
                conversion_result = convert_and_display(points_to_convert)
                if conversion_result is not None:
                    AIRTIME().send(conversion_result)
            else:
                messagebox.showerror("Invalid Points", "Points to convert must be above 5 but less than or equal to your number of streaks.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number of points to convert.")
    else:
        messagebox.showerror("File Not Found", "The 'streak.txt' file was not found.")
