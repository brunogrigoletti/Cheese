import os
import tkinter as tk
import pyautogui
import time
import threading


def move_mouse():
    while True:
        pyautogui.moveRel(100, 100)
        time.sleep(1)
        pyautogui.moveRel(-200, 0)
        time.sleep(1)
        pyautogui.moveRel(100, -100)
        time.sleep(3)

root = tk.Tk()
root.geometry("400x100")
root.title("Cheese")

icon_path = os.path.join(os.path.dirname(__file__), 'Cheese.ico')
root.iconbitmap(icon_path)

label = tk.Label(root, text="Mouse will move every 2 minutes!", anchor='center')
label.pack(expand=True)

thread = threading.Thread(target=move_mouse, daemon=True)
thread.start()

root.mainloop()