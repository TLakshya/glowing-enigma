import pyautogui
import time
import tkinter as tk

root = tk.Tk()
root.title("Pixel Color Viewer")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

color_box = canvas.create_rectangle(0, 0, 200, 200, fill='black')

label = tk.Label(root, text="Move your mouse to see color", font=("Arial", 14))
label.pack()

def update_color():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    canvas.itemconfig(color_box, fill=hex_color)
    label.config(text=f"({x}, {y}) RGB({r}, {g}, {b}) {hex_color}")
    root.after(100, update_color)

update_color()
root.mainloop()
