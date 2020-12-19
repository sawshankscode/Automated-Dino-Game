import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(375, 425):
        for j in range(410, 570):
            if data[i, j] < 100:
                hit("down")
                return True

    for i in range(400, 450):
        for j in range(570, 650):
            if data[i, j] < 100:
                hit("up")
                return True
    return False

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit("up") 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        # isCollide(data)
            
        # print(asarray(image))
        
        # Draw the rectangle for cactus
        for i in range(400, 450):
            for j in range(570, 650):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(375, 425):
            for j in range(410, 570):
                data[i, j] = 171

        image.show()
        break
      

