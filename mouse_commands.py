import win32api, win32con
from win32api import GetSystemMetrics
DIST_THRESH = 20
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

class Mouse:
    SCROLL_INVERSE_GAIN = 20
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
        x = width + width//10 - x * width//250
        y = - width/10 + y * width//250
        if x < 0:
            x = 0;
        if y < 0:
            y = 0;
        if x >= width:
            x = width;
        if y >= width:
            y = width;
        center = (self.init_x, self.init_y)
        point = (x, y)
        if not self.clicked or distance(point, center) > DIST_THRESH:
            win32api.SetCursorPos((x, y))
            self.x, self.y = x, y
        else:
            win32api.SetCursorPos((self.init_x, self.init_y))
            self.x, self.y = self.init_x, self.init_y

    def get_pos(self):
        return win32api.GetCursorPos()

    def scroll(self): # positive direction = up or right
        if not self.scrolling:
            print("Started to scroll!")
            self.init_x, self.init_y = win32api.GetCursorPos()
        self.scrolling = True
        h_direction, v_direction = self.x - self.init_x, self.y - self.init_y
        print(self.x, self.init_x)
        print self.y, self.init_y
        print h_direction, v_direction
        v_direction = v_direction // self.SCROLL_INVERSE_GAIN # decrease effect
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
sqrt = lambda x: x ** 0.5
def distance(point1, point2):
    return (((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))**(1/2)
