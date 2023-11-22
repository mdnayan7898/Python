import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Camera App")

        self.capture_button = ttk.Button(self.master, text="Capture", command=self.capture_image)
        self.capture_button.pack(pady=10)

        self.image_label = ttk.Label(self.master)
        self.image_label.pack()

        self.video_source = 0  # Default camera index
        self.cap = cv2.VideoCapture(self.video_source)

        self.update()

    def capture_image(self):
        ret, frame = self.cap.read()

        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.display_image(image)

    def update(self):
        ret, frame = self.cap.read()

        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.display_image(image)

        self.master.after(10, self.update)

    def display_image(self, image):
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

def main():
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
