import keyboard
import mouse
import time

from screeninfo import get_monitors

screen_width = 0
screen_height = 0

def get_screen_dimensions():
    global screen_width, screen_height
    monitors = get_monitors()
    for monitor in monitors:
        screen_width = monitor.width
        screen_height = monitor.height
        print(f"Width: {monitor.width}, Height: {monitor.height}")
get_screen_dimensions()


def walkForward():
    keyboard.press('w')

def stepForward():
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.release('w')

def walkBackwards():
    keyboard.press('s')

def stepBackward():
    keyboard.press('s')
    time.sleep(0.3)
    keyboard.release('s')

def walkRight():
    keyboard.press('d')

def walkLeft():
    keyboard.press('a')

def keysRelease():
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('d')
    keyboard.release('a')
    mouse.release(button='left')


def mine():
    mouse.press(button='left')
    time.sleep(0.9)

def mineRelease():
    mouse.release(button='left')


def lookRight():
    #Testing on 2880 x 1800 Laptop, turns right mostly 90 degrees
    mouse.move(54,0,absolute=False,duration=1)

def lookLeft():
    mouse.move(-54,0,absolute=False,duration=1)

def lookDown():
    mouse.move(0,54,absolute=False,duration=1)

def lookUp():
    mouse.move(0,-23,absolute=False,duration=1)
