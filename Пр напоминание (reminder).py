from tkinter import *
from tkinter messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание")
label.pack(pady=10)
set_buton = Button(text="Установить напоминание", command=set)
set_buton.pack()

window.mainloop()


