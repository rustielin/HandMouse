class Mouse:
    def __init__(self):
        self.clicked = False
        self.scrolling = False
        self.init_x = 0 # for scrolling
        self.init_y = 0
        self.x, self.y = win32api.GetCursorPos()

    def get_pos(self):
        return win32api.GetCursorPos()

    def left_click(self):
        if self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.x, self.y, 0, 0) #click is true
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.x, self.y, 0, 0)
        self.clicked = True #prevents new action from happening before reset

    def left_press(self):
        if self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.x, self.y, 0, 0)
        self.clicked = True

    def left_unpress(self):
        if not self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.x, self.y, 0, 0)
        self.clicked = False

    def right_click(self):
        if self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, self.x, self.y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, self.x, self.y, 0, 0)

    def right_press(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)

    def right_unpress(self):
        if not self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, self.x, self.y, 0, 0)
        self.clicked = False

    def set_mouse(self, x, y):
        win32api.SetCursorPos((x, y))

    def scroll(self): # positive direction = up or right
        h_direction, v_direction = self.x - self.init_x, self.y - self.init_y
        v_direction = v_direction // SCROLL_INVERSE_GAIN # decrease effect
        #win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, x, y, h_direction, 0) # for sideways scrolling
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, self.x, self.y, v_direction, 0)
        self.clicked = True

    def reset(self):
        self.left_unpress()
        self.right_unpress()
        self.__init__()

mouse = Mouse()

def scroll():
    if not mouse.scrolling:
        mouse.init_x, mouse.init_y = win32api.GetCursorPos()
    mouse.scrolling = True
    mouse.scroll()

def check_gesture(num):
    
