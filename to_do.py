import tkinter
from tkinter import *
import os
import ast
import threading
import time
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import winsound
import africastalking
import dotenv
from dotenv import load_dotenv
import openai

# Set your OpenAI API key here
openai.api_key = ""

load_dotenv()
api_key_path = os.getenv("API_KEY")

root = Tk()
root.title("Convertify")
root.geometry("400x650+400+100")
root.resizable(False, False)


task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END, task)


def deleteTask():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        list_box.delete(ANCHOR)

def exit():
    root.destroy()
    import signin

# create a tasklist.txt file


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                list_box.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close()


# Initialize streak count
streak_count = 0

# Check if the streak file exists and load the streak count
if os.path.isfile('streak.txt'):
    with open('streak.txt', 'r') as file:
        streak_count = int(file.read())


# Function to send a notification and SMS
def send_notification():
    if not stop_notifications:
        messagebox.showinfo("Notification", gen_notification_message)
        play_notification_sound()
        send_sms_notification()
        # Schedule the next notification
        root.after(notification_interval * 1000, send_notification)

# Function to play the continuous beeping sound


def play_notification_sound():
    # Play a continuous beeping sound for approximately 3 seconds
    end_time = time.time() + 3  # Sound will play for 3 seconds
    while time.time() < end_time:
        winsound.Beep(2000, 500)  # Play a 2000 Hz beep for 500 milliseconds

# Function to send an SMS notification using Africa's Talking


def send_sms_notification():
    global gen_notification_message
    try:
        # Replace with your Africa's Talking API credentials

        # initialize africastalking
        africastalking.initialize(
            username='BADS',
            api_key=api_key_path
        )

        # Create an SMS service
        sms = africastalking.SMS

        # Read recipient's phone number from datasheet.txt
        recipient_phone_number = get_recipient_phone_number()

        if recipient_phone_number:
            # Define the SMS message
            sms_message = f"Notification: {gen_notification_message}"

            # Send the SMS
            response = sms.send(sms_message, [recipient_phone_number])
            print(response)
        else:
            print("Recipient's phone number not found in datasheet.txt")

    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# Function to get recipient's phone number from datasheet.txt


def get_recipient_phone_number():
    try:
        with open('datasheet.txt', 'r') as file:
            data = file.read()
            data_dict = eval(data)
            return data_dict.get('phone', None)
    except Exception as e:
        print(f"Error reading datasheet.txt: {str(e)}")
        return None
###################
# Function to start scheduling notifications
def start_notifications():
    global stop_notifications
    global notification_message
    global notification_interval
    global gen_notification_message

    notification_message = simpledialog.askstring(
        "Notification Message", "Enter your notification message:")
    
    if notification_message:
        # Prompt the user for the notification interval in seconds
        notification_interval = simpledialog.askinteger(
            "Notification Interval", "Enter notification interval (in seconds):")
        
    if notification_message:
            # Generate a notification message using OpenAI's GPT-3 model
            response = openai.Completion.create(
            engine="davinci",
            prompt=f"Please notify the user about the latest updates on '{notification_message}'.",
            max_tokens=50  # Adjust the token limit as needed
            )
            gen_notification_message = response.choices[0].text

            # Send the notification (you can customize this part)
            #send_notification(notification_message)

            if notification_interval:
                stop_notifications = False
                send_notification()


""" def start_notifications():
    global stop_notifications
    global notification_message
    global notification_interval

    # Prompt the user for the notification message
    notification_message = simpledialog.askstring(
        "Notification Message", "Enter your notification message:")

    if notification_message:
        # Prompt the user for the notification interval in seconds
        notification_interval = simpledialog.askinteger(
            "Notification Interval", "Enter notification interval (in seconds):")

        if notification_interval:
            stop_notifications = False
            send_notification() """

# Function to stop notifications


def stop_notifications():
    global stop_notifications
    stop_notifications = True


# Function to celebrate
def celebrate():
    root.destroy()
    import animate

def withdraw_streaks():
    try:
        root.destroy()
        import to_airtime
        print("success")
    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")

# icon
icon_path = os.path.join("images", "task.png")
img_icon = PhotoImage(file=icon_path)
root.iconphoto(False, img_icon)

# top bar
top_img_path = os.path.join("images", "topbar.png")
top_img = PhotoImage(file=top_img_path)
Label(root, image=top_img,).pack()

# dock
dock_img_path = os.path.join("images", "dock.png")
dock_img = PhotoImage(file=dock_img_path)
Label(root, image=dock_img, bg='#32405b').place(x=30, y=25)

# noteImage
note_img_path = os.path.join("images", "task.png")
note_img = PhotoImage(file=note_img_path)
Label(root, image=note_img, bg='#32405b').place(x=340, y=25)

# heading
heading = Label(root, text="Convertify", font=(
    "Arial", 20, "bold"), bg="#32405b", fg="white")
heading.place(x=130, y=20)

# Create a label to display the streak count
streak_label = Label(
    root, text=f"Streaks🔥: {streak_count} days", font=("Arial", 16))
streak_label.pack(pady=10)

#withdrawing streaks
withdraw = Button(root, text="Convert streaks to airtime?", font=("Arial", 10, "bold"),
                 fg="#57a1f8", border=0, cursor="hand2", command=withdraw_streaks)
withdraw.place(x=100, y=125)

# Create a frame to contain the buttons
button_frame = Frame(root)
button_frame.pack(pady=30)

# Create a button to start scheduling notifications
start_button = Button(button_frame, text="Start Notification", font=("Arial", 10, "bold") , command=start_notifications)
start_button.pack(side=LEFT, padx=10)

# Create a button to stop notifications
stop_button = Button(button_frame, text="Stop Notifications",font=("Arial", 10, "bold"), command=stop_notifications)
stop_button.pack(side=LEFT, padx=10)

# Time interval (in seconds) between notifications (e.g., 10 seconds)
# notification_interval = 3

# Flag to control notifications
notification_message = ""
stop_notifications = False

# Main frame
frame = Frame(root, width=400, height=30, bg="white")
frame.place(x=0, y=220)


# Create a task input
task = StringVar()
task_entry = Entry(frame, width=18, font=("Arial", 15), bd=0)
task_entry.place(x=10, y=7)

# Create a add button
button = Button(frame, text="Add", font=("Arial", 15, "bold"),
                bg="#32405b", fg="white", bd=0, command=addTask)
button.place(x=340, y=0)

# Create a list frame
frame1 = Frame(root, bd=3, width=700, height=230, bg="#32405b")
frame1.pack(pady=(70, 0))

# Create a list box
list_box = Listbox(frame1, width=40, height=13, font=(
    "Arial", 12), bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
list_box.pack(side=LEFT, fill=BOTH, padx=2)

# Create a scroll bar
scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=BOTH)

# Set scroll to listbox
list_box.config(yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)


openTaskFile()


#Done button
done_button = Button(root, text="Done", font=("Arial", 13, "bold"), command=celebrate)
done_button.pack(pady=8)


# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(side=BOTTOM, pady=10)

# Delete button
delete_icon_path = os.path.join("images", "delete.png")
delete_icon = PhotoImage(file=delete_icon_path)
delete_button = Button(button_frame, image=delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=LEFT, padx=0)  # Place the delete button to the left of the frame

# Exit button
exit_icon_path = os.path.join("images", "exit.png")
exit_icon = PhotoImage(file=exit_icon_path)
exit_button = Button(button_frame, image=exit_icon, bd=0, command=exit)
exit_button.pack(side=RIGHT, padx=15)  # Place the exit button to the left of the frame


root.mainloop()
