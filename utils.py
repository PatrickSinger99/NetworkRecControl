from ctypes import windll, Structure, c_long, byref


def load_env(path=".env"):
    env = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


def get_taskbar_height():

    class RECT(Structure):
        _fields_ = [("left", c_long), ("top", c_long), ("right", c_long), ("bottom", c_long)]

    # Get full screen size
    screen = RECT()
    windll.user32.SystemParametersInfoW(0x0030, 0, byref(screen), 0)  # Work area
    screen_width = windll.user32.GetSystemMetrics(0)
    screen_height = windll.user32.GetSystemMetrics(1)

    # Work area (excludes taskbar)
    work_area = RECT()
    windll.user32.SystemParametersInfoW(0x0030, 0, byref(work_area), 0)

    # If taskbar is horizontal (bottom or top)
    taskbar_height = screen_height - (work_area.bottom - work_area.top)

    # If taskbar is vertical (left or right), height remains full, width is reduced
    taskbar_width = screen_width - (work_area.right - work_area.left)

    if taskbar_height > 0:
        return taskbar_height
    elif taskbar_width > 0:
        return 0  # Taskbar is on the side
    else:
        return 0  # Taskbar is hidden or full screen
