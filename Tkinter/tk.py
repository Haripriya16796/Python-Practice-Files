import tkinter as tk
# 1 usage
def say_hello():
    print('Hello tkinter!')
# the below will create a UI window
window = tk.Tk()
window.geometry('300x200+10+10')
# below is widgets---button widgets
button = tk.Button(window, text = 'say hello', command = say_hello)
button.pack()
# the below lisents to events done by user
window.mainloop()