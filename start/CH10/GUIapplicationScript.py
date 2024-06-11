import tkinter as tk

root = tk.Tk()
root.title("My GUI Application")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button
def button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click me", command=button_click)
button.pack()

root.mainloop()
