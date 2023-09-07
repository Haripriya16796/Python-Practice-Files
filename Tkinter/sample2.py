import tkinter as tk

def on_button_click():
    label.config(text = 'Hello tkinter')
    # button.config(text = 'Hello tkinter')

# create main application window
root = tk.Tk()

# set the window title
root.title('tkinter example')

root.geometry('300x150')

label = tk.Label(root, text = 'click the button to change this')
label.pack(pady=20)

button = tk.Button(root, text = 'click me', command = on_button_click)
button.pack()


# the below lisents to events done by user
root.mainloop()