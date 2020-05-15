from tkinter import *
from tkinter import ttk
root = Tk()
root.configure(bg="brown")
root.geometry('700x500')
root.title('Facial Detection app')

#add background image
background_image = PhotoImage(file="bg.gif")
background_label= Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#button to proceed
button = ttk.Button(root,  text="BEGIN")
button.pack(side=RIGHT, padx=100,pady=100)
