import os
import tkinter as tk
import pyautogui
import time
import threading


def move_mouse():
    while True:
        pyautogui.press('space')
        pyautogui.press('space')
        pyautogui.press('space')
        time.sleep(840)

root = tk.Tk()
root.geometry("400x100")
root.title("Triple Jump")

icon_path = os.path.join(os.path.dirname(__file__), 'Jump.ico')
root.iconbitmap(icon_path)

label = tk.Label(root, text="You'll triple jump every 14 minutes!", anchor='center')
label.pack(expand=True)

thread = threading.Thread(target=move_mouse, daemon=True)
thread.start()

root.mainloop()