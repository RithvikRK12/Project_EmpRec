import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Function to update video frames in Tkinter window
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert frame from OpenCV BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the image to a format Tkinter can use
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        # Update the image in the label
        label.config(image=imgtk)
        label.image = imgtk
    # Schedule next frame update
    root.after(10, update_frame)

# Initialize Tkinter window
root = tk.Tk()
root.title("Tkinter Video Background")

# Load the video using OpenCV
cap = cv2.VideoCapture("mp4video.mp4")

# Create a label to hold the video frames
label = tk.Label(root)
label.pack()

# Start updating frames
update_frame()

# Run the Tkinter event loop
root.mainloop()

# Release the video capture on close
cap.release()
