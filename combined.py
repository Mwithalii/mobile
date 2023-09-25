import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import threading
import time
import winsound

# Function to send a notification
def send_notification():
    if not stop_notifications:
        messagebox.showinfo("Notification", notification_message)
        play_notification_sound()
        # Schedule the next notification
        root.after(notification_interval * 1000, send_notification)

# Function to play the notification sound (Windows)
def play_notification_sound():
    winsound.Beep(100, 50000)  # Play a 1000 Hz sound for 500 milliseconds

# Function to start scheduling notifications
def start_notifications():
    global stop_notifications
    global notification_message
    global notification_interval

    # Prompt the user for the notification message
    notification_message = simpledialog.askstring("Notification Message", "Enter your notification message:")

    if notification_message:
        # Prompt the user for the notification interval in seconds
        notification_interval = simpledialog.askinteger("Notification Interval", "Enter notification interval (in seconds):")

        if notification_interval:
            stop_notifications = False
            send_notification()

# Function to stop notifications
def stop_notifications():
    global stop_notifications
    stop_notifications = True

# Create the main tkinter window
root = tk.Tk()
root.title("Notification Scheduler")
root.geometry("300x300")

# Create a button to start scheduling notifications
start_button = tk.Button(root, text="Start Notifications", command=start_notifications)
start_button.pack(pady=20)

# Create a button to stop notifications
stop_button = tk.Button(root, text="Stop Notifications", command=stop_notifications)
stop_button.pack()

# Default notification message and interval
notification_message = ""
notification_interval = 10

# Variable for flag to control notifications
stop_notifications = False

root.mainloop()
