import pyautogui
import time

def automate_keyboard_actions():
    pyautogui.screenshot('screenshot.png')
    pyautogui.write('Hello, World!', interval=0.2)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'v')


if __name__ == '__main__':
    time.sleep(5)
    automate_keyboard_actions()