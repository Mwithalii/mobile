import tkinter as tk
import winsound
import os
import time
import threading  # Import the threading module

# Function to animate floating emojis
def animate_emojis():
    x, y = 50, 50  # Initial position
    for emoji in emojis:
        canvas.create_image(x, y, image=emoji)
        canvas.update()
        time.sleep(0.5)  # Delay between emojis (adjust as needed)
        canvas.delete("all")
        x += 50  # Adjust the spacing between emojis

# Function to play sound in a separate thread
def play_sound():
    winsound.PlaySound("pop.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Function to celebrate
def celebrate():
    done_button.pack_forget()
    canvas.pack()
    
    # Create a thread for sound playback
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()
    
    animate_emojis()
    
    # Wait for the sound thread to finish before showing the "Done" button
    sound_thread.join()
    
    canvas.pack_forget()
    done_button.pack()

# Create the main tkinter window
root = tk.Tk()
root.title("Celebration")

# Emojis as images (replace with your emoji images)
emoji_img_path = os.path.join("images", "emoji.png")
emoji_img = tk.PhotoImage(file=emoji_img_path)

ribbon_img_path = os.path.join("images", "ribbon.png")
ribbon_img = tk.PhotoImage(file=ribbon_img_path)

emoji1_img_path = os.path.join("images", "emoji1.png")
emoji1_img = tk.PhotoImage(file=emoji1_img_path)

emojis = [emoji_img,
          ribbon_img,
          emoji1_img]

# Create a canvas
canvas = tk.Canvas(root, width=300, height=150)

# Create a "Done" button
done_button = tk.Button(root, text="Done", command=celebrate)
done_button.pack(pady=20)

root.mainloop()
