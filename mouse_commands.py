import win32api, win32con


class Mouse:
    def __init__(self):
        self.clicked = False

    def get_pos(self):
        return win32api.GetCursorPos()

    def left_click(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #click is true
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        self.clicked = True #unclicks

    def left_press(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        self.clicked = True

    def left_unpress(self):
        if not self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        self.clicked = False

    def right_click(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    def right_press(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)

    def right_unpress(self):
        if not self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
        self.clicked = False

    def set_mouse(self, x, y):
        win32api.SetCursorPos((x, y))

    def scroll(self): #positive direction = up or right
        x, y = win32api.GetCursorPos()
        v_direction, h_direction = x - self.init_x, y - self.init_y
        win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, v_direction, 0)
        win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, h_direction, 0)
        self.clicked = True

    def reset(self):
        self.left_unpress()
        self.right_unpress()
        self.init_x = None
        self.init_y = None
        self.clicked = False

mouse = Mouse()
