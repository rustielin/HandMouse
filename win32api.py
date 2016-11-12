import win32api, win32con


clicked = False #does not allow new clicking function to run if another one is still active

def left_click():
    if clicked:
        return #protects from infinite clicks
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #click is true
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #unclicks
    clicked = True

def left_press():
    if clicked:
        return
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #click is true
    clicked = True

def left_unpress():
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #unclicks
    clicked = False

def right_click():
    if clicked:
        return
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0) #click is true
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0) #unclicks
    clicked = True

def right_press():
    if clicked:
        return
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0) #click is true
    clicked = True

def right_unpress():
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0) #unclicks
    clicked = False


def set_mouse(x, y):
    win32api.SetCursorPos((x, y))

def scroll(v_direction, h_direction): #positive direction = up or right
    win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, v_direction, 0)
    win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, h_direction, 0)
    clicked = True

def reset():
    clicked = False
    left_unpress()
    right_unpress()
