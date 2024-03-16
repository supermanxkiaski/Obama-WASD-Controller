import os
import tkinter as tk
from PIL import Image, ImageTk
import keyboard  # You might need to install this library using pip

# Directories containing the images for each key
image_dirs = {
    'w': r'C:\Users\super\Desktop\ObamaController\w',
    'a': r'C:\Users\super\Desktop\ObamaController\key',
    's': r'C:\Users\super\Desktop\ObamaController\s',
    'd': r'C:\Users\super\Desktop\ObamaController\d'
}

# List of image files for each key
image_files = {
    key: [os.path.join(dir, img) for img in os.listdir(dir) if img.endswith('.png')]
    for key, dir in image_dirs.items()
}

# Sort the image files
for files in image_files.values():
    files.sort()

# Create a Tkinter window
root = tk.Tk()

# Create a label and add it to the window
label = tk.Label(root)
label.pack()

# Index of the current image for each key
current_images = {key: 0 for key in image_dirs.keys()}

def update_image():
    global current_images

    # Check if a key is being pressed
    for key, files in image_files.items():
        if keyboard.is_pressed(key):  # Check if the key is being pressed
            # Open the current image
            pil_image = Image.open(files[current_images[key]])

            # Convert the PIL image to a Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the label with the new image
            label.config(image=tk_image)
            label.image = tk_image

            # Move to the next image
            current_images[key] = (current_images[key] + 2) % len(files)
            break  # Exit the loop as soon as a key is found to be pressed

    # Schedule the next update
    root.after(3, update_image)

# Start the updates
update_image()

# Start the Tkinter event loop
root.mainloop()
