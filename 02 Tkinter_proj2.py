# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:55:18 2023

@author: Lenovo
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter Get File Dialog')
root.resizable(False, False)
root.geometry('350x200')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    f = filename.split("/")
    showinfo(
        title='Selected File',
        message=f[-1]
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

# run the application
root.mainloop()

