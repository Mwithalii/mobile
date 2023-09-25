import tkinter
from tkinter import *
import os
import ast
import threading
import time
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

root=Tk()
root.title("TO DO List")
root.geometry("400x650+400+100")
root.resizable(False, False)


task_list = []


def addTask():
    task=task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END, task)

def deleteTask():
    global task_list
    task=str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        list_box.delete(ANCHOR)

#create a tasklist.txt file
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                list_box.insert(END, task)
    except:
        file=open("tasklist.txt", "w")
        file.close()

# Initialize streak count
streak_count = 0

# Check if the streak file exists and load the streak count
if os.path.isfile('streak.txt'):
    with open('streak.txt', 'r') as file:
        streak_count = int(file.read())


# Function to send a notification
def send_notification():
    if not stop_notifications:
        messagebox.showinfo("Notification", notification_message)
        # Schedule the next notification
        root.after(notification_interval * 1000, send_notification)

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

#icon
icon_path = os.path.join("images", "task.png")
img_icon = PhotoImage(file=icon_path)
root.iconphoto(False, img_icon)

#top bar
top_img_path = os.path.join("images", "topbar.png")
top_img = PhotoImage(file=top_img_path)
Label(root, image=top_img,).pack()

#dock
dock_img_path = os.path.join("images", "dock.png")
dock_img = PhotoImage(file=dock_img_path)
Label(root, image=dock_img, bg='#32405b').place(x=30, y=25)

#noteImage
note_img_path = os.path.join("images", "task.png")
note_img = PhotoImage(file=note_img_path)
Label(root, image=note_img, bg='#32405b').place(x=340, y=25)

#heading
heading=Label(root, text="TO DO List", font=("Arial", 20, "bold"), bg="#32405b", fg="white")
heading.place(x=130, y=20)

# Create a label to display the streak count
streak_label = Label(root, text=f"Streaks🔥: {streak_count} days", font=("Arial", 16))
streak_label.pack(pady=0)

# Create a button to start scheduling notifications
start_button = Button(root, text="Start Notifications", command=start_notifications)
start_button.pack(padx=0, pady=10)

# Create a button to stop notifications
stop_button = Button(root, text="Stop Notifications", command=stop_notifications)
stop_button.pack(padx=15)

# Time interval (in seconds) between notifications (e.g., 10 seconds)
#notification_interval = 3

# Flag to control notifications
notification_message = ""
stop_notifications = False

#Main frame
frame=Frame(root, width=400, height=40, bg="white")
frame.place(x=0, y=200)


#Create a task input
task = StringVar()
task_entry=Entry(frame, width=18, font=("Arial", 20), bd=0)
task_entry.place(x=10, y=7)

#Create a add button
button=Button(frame, text="Add", font=("Arial", 19, "bold"), bg="#32405b", fg="white", bd=0, command=addTask)
button.place(x=300, y=0)

#Create a list frame
frame1=Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(100,0))

#Create a list box
list_box=Listbox(frame1, width=40, height=13, font=("Arial", 12), bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
list_box.pack(side=LEFT, fill=BOTH, padx=2)

#Create a scroll bar
scroll=Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=BOTH)

#Set scroll to listbox
list_box.config(yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)


openTaskFile()


#delete
delete_icon_path = os.path.join("images", "delete.png")
delete_icon = PhotoImage(file=delete_icon_path)
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)


root.mainloop()