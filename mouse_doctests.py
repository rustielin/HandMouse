from mouse_commands import *
import time
import test

mouse = Mouse()

def tests():
    #v, h = 1, 1
    while True:
        # time.sleep(0.01)
        # mouse.x, mouse.y = mouse.get_pos()
        # if mouse.x == 0 or mouse.x == width:
        #     h = -h
        # if mouse.y == 0 or mouse.y == height:
        #     v = -v
        # print(mouse.x, mouse.y, h, v)
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, h, v)

        #back_and_forth()

        # mouse.set_pos(50, 50)
        # time.sleep(0.5)
        # mouse.right_press()
        # mouse.left_press()
        mouse.x, mouse.y = mouse.get_pos()
        #mouse.scroll()
        
tests()

def back_and_forth():
    mouse.set_pos(100, 50)
    time.sleep(0.5)
    mouse.left_press()
    time.sleep(0.5)
    mouse.set_pos(50, 50)
    time.sleep(0.5)
    mouse.left_unpress()
    time.sleep(0.5)
    mouse.left_press()
    time.sleep(0.5)
    mouse.set_pos(100, 50)
    time.sleep(0.5)
    mouse.left_unpress()
    time.sleep(0.5)
