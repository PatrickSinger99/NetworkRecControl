import tkinter as tk
from sys import set_int_max_str_digits

from screeninfo import get_monitors
from utils import *
from tkinter.font import Font


class NumSelector(tk.Frame):
    def __init__(self, *args, min_val=0, max_val=9, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(bg=self.master.cget("bg"))

        self.min_val = min_val
        self.max_val = max_val

        self.up_btn = tk.Button(self, text="+", command=self._on_up, font=Font(size=20, weight="bold"),
                                bg=self.cget("bg"), fg="white", cursor="hand2", bd=0, relief="flat")
        self.up_btn.pack(side="top", fill="x")

        self.num = tk.IntVar(value=0)
        self.num_display = tk.Label(self, textvariable=self.num, font=Font(size=20), bg=self.cget("bg"), fg="white")
        self.num_display.pack(side="top", fill="x")

        self.down_btn = tk.Button(self, text="-", command=self._on_down, font=Font(size=20, weight="bold"),
                                  bg=self.cget("bg"), fg="white", cursor="hand2", bd=0, relief="flat")
        self.down_btn.pack(side="top", fill="x")

    def _on_up(self):
        cur = self.num.get()
        if cur + 1 > self.max_val:
            self.num.set(self.min_val)
        else:
            self.num.set(cur + 1)

    def _on_down(self):
        cur = self.num.get()
        if cur - 1 < self.min_val:
            self.num.set(self.max_val)
        else:
            self.num.set(cur - 1)

    def get(self):
        return self.num.get()

    def disable(self):
        self.up_btn.config(fg="grey", cursor="", bg=self.cget("bg"))
        self.down_btn.config(fg="grey", cursor="", bg=self.cget("bg"))
        self.num_display.config(fg="grey", bg=self.cget("bg"))

    def enable(self):
        self.up_btn.config(fg="white", cursor="hand2", bg=self.cget("bg"))
        self.down_btn.config(fg="white", cursor="hand2", bg=self.cget("bg"))
        self.num_display.config(fg="white", bg=self.cget("bg"))


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

        # Body Frame

        self.body = tk.Frame(self.base, bg=self.base.cget("bg"))
        self.body.pack(side="top", fill="both", expand=True)

        # Time Selection

        self.time_selector = tk.Frame(self.body, bg=self.body.cget("bg"))
        self.time_selector.pack(side="left")

        self.hour_selector = NumSelector(self.time_selector)
        self.hour_selector.pack(side="left")

        tk.Label(self.time_selector, text="hrs", bg=self.time_selector.cget("bg"), font=Font(size=16),
                 fg="white").pack(side="left")

        self.first_min_selector = NumSelector(self.time_selector, max_val=5)
        self.first_min_selector.pack(side="left")

        self.sec_min_selector = NumSelector(self.time_selector)
        self.sec_min_selector.pack(side="left")

        tk.Label(self.time_selector, text="mins", bg=self.time_selector.cget("bg"), font=Font(size=16),
                 fg="white").pack(side="left")

        self.timer_elems = (self.hour_selector, self.first_min_selector, self.sec_min_selector)

        # Actions

        self.recording = False
        self.btn_text = {False: "Start Recording", True: "Stop Recording"}
        self.rec_btn = tk.Button(self.body, text=self.btn_text[self.recording], cursor="hand2", fg="white", bd=0,
                                 font=Font(size=18), command=self._on_rec_press, bg=self.body.cget("bg"), relief="flat")
        self.rec_btn.pack()

    def _on_rec_press(self):
        if self.recording is False:
            self.recording = True
            self.rec_btn.config(text=self.btn_text[self.recording], fg="red")
            for elem in self.timer_elems:
                elem.disable()
        else:
            self.recording = False
            self.rec_btn.config(text=self.btn_text[self.recording], fg="white")
            for elem in self.timer_elems:
                elem.enable()

    def get_timer_seconds(self):
        hrs = self.hour_selector.get()
        minutes = self.first_min_selector.get() * 10 + self.sec_min_selector.get()
        return hrs * 3600 + minutes * 60

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
