import pyautogui
import time

# Pause to switch to the game window
print("Starting in 3 seconds... Go to your game window!")
time.sleep(3)

# Coordinates where obstacles appear
# You must adjust x, y to match the position in YOUR game!
x, y = 195,615
day = (255,255,255)

while True:
    pixel_colortop = pyautogui.pixel(1123, 344)
    # Get the color of the pixel at (x, y)
    pixel_color = pyautogui.pixel(x, y)
    if pixel_colortop[0] is day[0] :
        print('day')
        # Check if it's dark enough (black or close to black)
        if pixel_color[0] < 100 and pixel_color[1] < 100 and pixel_color[2] < 100:
            pyautogui.press('space')
            print("JumpDay!")
    else:
        print('night')
        if pixel_color[0] > 100 and pixel_color[1] > 100 and pixel_color[2] > 100:

            pyautogui.press('space')
            print("Jump!")


    # Add a tiny sleep so it doesn't overload CPU
    time.sleep(0.01)
