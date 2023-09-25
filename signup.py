from tkinter import *
from tkinter import messagebox
import os
import ast
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

sms = africastalking.SMS


window=Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.resizable(False, False)
window.config(bg="white")




def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    mail=email.get()
    hone=phone.get()

    if password==confirm_password:
        try:
            file = open('datasheet.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password, "email":mail, "phone":hone}
            r.update(dict2)
            file.truncate(0)
            file.close()

            """ print(r.keys())
            print(r.values()) """ 


            file = open('datasheet.txt', 'w')
            w=file.write(str(r))
            
            
            message = f"Hello {username}, your account has been created successfully!"
            response = sms.send(message, [hone])
            print(response)

            messagebox.showinfo("Success!", "Account created successfully!")

            
        
        except:
            file=open('datasheet.txt', 'w')
            pp=str({username:password , "email":mail, "phone":hone})
            file.write(pp)
            file.close()
    
    else:
        messagebox.showerror("Error!", "Password does not match!")



def sign():
    window.destroy()
    import signin



img_path = os.path.join("images", "sign_up.png")
img = PhotoImage(file=img_path)
Label(window, image=img, bg="white").place(x=50, y=90)

frame = Frame(window, width=500, height=500, bg="white")
frame.place(x=400, y=15)


heading = Label(frame, text="Sign Up", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
heading.place(x=120, y=5)

# Create a username input
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0, "Username")

user = Entry(frame, font=("Arial", 15), bg="white", fg="black", width=25, border=0)
user.place(x=30, y=50)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=75)

# Create a password input
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        code.insert(0, "Password")

code = Entry(frame, font=("Arial", 15), bg="white", fg="black", width=25, border=0)
code.place(x=30, y=120)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=145)

# Create a confirm password input
def on_enter(e):
    confirm_code.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        confirm_code.insert(0, "Confirm Password")

confirm_code = Entry(frame, font=("Arial", 15), bg="white", fg="black", width=25, border=0)
confirm_code.place(x=30, y=190)
confirm_code.insert(0, "Confirm Password")
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=215)

# Create a email input
def on_enter(e):
    email.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        email.insert(0, "Email")

email = Entry(frame, font=("Arial", 15), bg="white", fg="black", width=25, border=0)
email.place(x=30, y=260)
email.insert(0, "Email")
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=285)

# Create a phone number input
def on_enter(e):
    phone.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        phone.insert(0, "Phone Number")

phone = Entry(frame, font=("Arial", 15), bg="white", fg="black", width=25, border=0)
phone.place(x=30, y=330)
phone.insert(0, "Phone Number")
phone.bind("<FocusIn>", on_enter)
phone.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=355)



#button
Button(frame, text="Sign Up", font=("Arial", 15, "bold"), bg="#57a1f8", fg="white",width=23, border=0, command=signup).place(x=35, y=380)
Label(frame, text="Already have an account?", font=("Arial", 10), bg="white", fg="black").place(x=90, y=420)

signin=Button(frame, text="Sign In", font=("Arial", 10, "bold"), bg="white", fg="#57a1f8", border=0, cursor="hand2", command=sign)
signin.place(x=250, y=420)


window.mainloop()