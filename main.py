from PIL import ImageGrab
import keyboard
import pyautogui
import time

play = 1
'''
while play:
    img = ImageGrab.grab((630, 290, 700, 350))
    px = img.getpixel((25, 30))
    print(px)
    if px == (158, 158, 158):

        pyautogui.keyDown("space")
        time.sleep(0.08)
        pyautogui.keyUp("space")
    if keyboard.is_pressed('e'):
        play = 0

'''
while play:
    if keyboard.is_pressed('e'):

        img = ImageGrab.grab((630, 290, 700, 350))
        img.save("ceva.jpg")
        px = img.getpixel((25, 30))
        print(px)
        if px == (172, 172, 172):
            pyautogui.keyDown("space")
            time.sleep(.08)
