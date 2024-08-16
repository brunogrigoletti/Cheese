import os
import tkinter as tk
import pyautogui
import time
import threading


def move_mouse():
    while True:
        current_position = pyautogui.position()
        new_x = current_position.x + 10
        new_y = current_position.y + 10
        
        pyautogui.moveTo(new_x, new_y)
        
        time.sleep(120)

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