import _tkinter
import random
import tkinter

#Root Window
root = tkinter.Tk()

#Functions
def add_task():
    pass





lbl_title = tkinter.Label(root, text="Task-Manager")
lbl_title.pack()

lbl_display = tkinter.Label(root, text="")
lbl_display.pack()

txt_input = tkinter.Entry(root, width=15)
txt_input.pack()

btn_add_task = tkinter.Button(root, text="Adauga Task", fg="green", command=add_task)
btn_add_task.pack()
root.mainloop()
