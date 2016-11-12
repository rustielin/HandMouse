import win32api, win32con

def left_click():
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #click is true
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #unclicks
