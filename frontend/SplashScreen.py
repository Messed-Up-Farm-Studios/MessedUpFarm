import time
import threading
import tkinter as tk
from tkinter import PhotoImage

from frontend.media_utils import resource_path

class Splashscreen:
    def __init__(self, duration=1500):

        def _center_window(win, width, height):
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()

            # Calculate position x, y
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)

            win.geometry(f"{width}x{height}+{x}+{y}")

        self.splash_root = tk.Tk()
        self.splash_root.overrideredirect(True)
        self.splash_root.configure(bg='white')

        width, height = 400, 300
        _center_window(self.splash_root, width, height)

        # Load image
        self.splash_image = PhotoImage(file=resource_path("resources/app.png"))
        label = tk.Label(self.splash_root, image=self.splash_image, bg='white')
        label.pack(expand=True)

        # Close after duration
        self.splash_root.after(duration, self.close_splash)

        self.splash_root.mainloop()

    def close_splash(self):
        self.splash_root.destroy()


    