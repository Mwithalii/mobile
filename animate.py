from tkinter import *
import time
import os
import random
import winsound

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1
window = Tk()

# Play the sound when the window opens
winsound.PlaySound("clap.wav", winsound.SND_ASYNC)

# Change the title of the window
window.title("Celebration!")

def on_closing():
    # Stop the sound when the window is closed
    winsound.PlaySound(None, winsound.SND_PURGE)
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo_path = os.path.join("images", "celebr.png")
background_photo = PhotoImage(file=background_photo_path)
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

text = canvas.create_text(250, 250, text="Congratulations on finishing today's tasks \n Keep up the good work 👏👏!", fill="white", font=("Arial", 15))

photo_image_path = os.path.join("images", "emoji.png")
photo_image = PhotoImage(file=photo_image_path)
image_width = photo_image.width()
image_height = photo_image.height()

def reset_image_position():
    # Randomly reposition the animation image
    x = random.choice([0, WIDTH - image_width])
    y = random.choice([0, HEIGHT - image_height])
    canvas.coords(my_image, x, y)

my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

while True:
    coordinates = canvas.coords(my_image)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] <= 0:
        xVelocity = -xVelocity
        reset_image_position()  # Reset position when animation exits the window
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] <= 0:
        yVelocity = -yVelocity
        reset_image_position()  # Reset position when animation exits the window

    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
