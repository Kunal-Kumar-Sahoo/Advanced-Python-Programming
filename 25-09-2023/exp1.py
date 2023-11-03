import pyautogui
import time

def automate_mouse_actions():
    pyautogui.moveTo(500, 500, duration=1)
    pyautogui.click()
    pyautogui.moveTo(800, 300, duration=1)
    pyautogui.alert(text='Action completed', title='Advanced Python', button='OK')


if __name__ == '__main__':
    time.sleep(5)
    automate_mouse_actions()
    screen_width, screen_height = pyautogui.size()
    print(screen_width, screen_height)