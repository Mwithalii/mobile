from tkinter import *
from tkinter import messagebox
import os
import ast

# Create a window
root = Tk()
root.title("Sign In")
root.geometry("925x500+300+200")
root.resizable(False, False)
root.config(bg="#262626")


def signin():
    username = user.get()
    password = code.get()


    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    """ print(r.keys())
    print(r.values()) """


    if username in r.keys() and password == r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.resizable(False, False)
        screen.config(bg="#262626")

        Label(screen, text="Welcome", font=("Arial", 20, "bold"), bg="#262626", fg="white").pack(expand=True)

    
    else:
        messagebox.showerror("Invalid!", "Invalid username or password!")
    
 
    screen.mainloop()
    root.destroy()  


def signup_command():
    root.destroy()
    import signup

#Include image
img_path = os.path.join("images", "login.png")
img = PhotoImage(file=img_path)
Label(root, image=img, bg="white").place(x=50, y=50)


# Create a frame
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign In", font=("Arial", 20, "bold"), bg="white", fg="#57a1f8")
heading.place(x=120, y=5)

# Create a username input
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0, "Username")

user=Entry(frame, width=25, fg="black", font=("Arial", 12, "bold"), bg="white", border=0)
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Create a password input
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        code.insert(0, "Password")

code=Entry(frame, width=25, fg="black", font=("Arial", 12, "bold"), bg="white", border=0)
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

#singin button and signup option
Button(frame, text="Sign In", font=("Arial", 12, "bold"), bg="#57a1f8", fg="white", border=0, width=29, pady=7, command=signin).place(x=30, y=204)
label=Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Arial", 9, "bold"))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign Up", font=("Arial", 9, "bold"), bg="white", fg="#57a1f8", border=0, cursor="hand2", command=signup_command)
sign_up.place(x=215, y=270)





root.mainloop()