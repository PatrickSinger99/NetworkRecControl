import tkinter as tk
from screeninfo import get_monitors
from utils import *
from tkinter.font import Font


class App(tk.Tk):
    cols = {"win_border": "#15191E", "win_main": "#222831"}

    def __init__(self):
        super().__init__()
        self.overrideredirect(True)  # Removes title bar and borders
        self.attributes("-topmost", True)  # Keeps the window always on top
        self.resizable(False, False)
        self.title("Network Stream Recorder")
        self._place_window(height=200, width=650)

        # Window Border
        self.config(bg=App.cols["win_border"])
        self.base = tk.Frame(self, bg=App.cols["win_main"])
        self.base.pack(fill="both", expand=True, padx=2, pady=2)

        # Header Frame

        self.header = tk.Frame(self.base, bg=self.base.cget("bg"))
        self.header.pack(side="top", fill="x")

        self.close_btn = tk.Button(self.header, text=" x ", command=self.destroy, font=Font(size=16))
        self.close_btn.pack(side="right")


    def _place_window(self, height, width):
        """Places the window at the bottom right corner"""

        # Get the screen dimension
        monitor = get_monitors()[0]  # Select main monitor
        screen_width = monitor.width
        screen_height = monitor.height
        taskbar_height = get_taskbar_height()

        # Calculate position x and y
        x = screen_width - width
        y = screen_height - height - taskbar_height

        # Set the geometry
        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
