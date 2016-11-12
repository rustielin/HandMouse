import win32api
from win32api import GetSystemMetrics
DIST_THRESH = 20

class Mouse:
    SCROLL_INVERSE_GAIN = 5
    def __init__(self):
        self.clicked = False
        self.scrolling = False
        self.init_x = 0 # for scrolling
        self.init_y = 0
        self.x, self.y = win32api.GetCursorPos()

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
        self.init_x = self.x
        self.init_y = self.y
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
        self.clicked = True

    def right_press(self):
        if self.clicked:
            return
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, self.x, self.y, 0, 0)
        self.init_x = self.x
        self.init_y = self.y
        self.clicked = True

    def right_unpress(self):
        if not self.clicked:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, self.x, self.y, 0, 0)
        self.clicked = False

    def set_pos(self, x, y):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        x = width -  x * width//200
        y = y * width//200
        center = (self.init_x, self.init_y)
        point = (x, y)
        if not clicked or distance(point, center) > DIST_THRESH:
            win32api.SetCursorPos((x, y))
            self.x, self.y = x, y
        else:
            win32api.SetCursorPos((self.init_x, self.init_y))
            self.x, self.y = self.init_x, self.init_y

    def scroll(self): # positive direction = up or right
        if not mouse.scrolling:
            mouse.init_x, mouse.init_y = win32api.GetCursorPos()
        mouse.scrolling = True
        h_direction, v_direction = self.x - self.init_x, self.y - self.init_y
        v_direction = v_direction // SCROLL_INVERSE_GAIN # decrease effect
        try:
            win32api.mouse_event(win32con.MOUSEEVENTF_HWHEEL, x, y, h_direction, 0) # for sideways scrolling
        except:
            pass #will skip if sidways scrolling not allowed
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, self.x, self.y, v_direction, 0)
        self.clicked = True

    def reset(self):
        self.left_unpress()
        self.right_unpress()
        self.__init__()

def distance(point1, point2):
    return sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))
