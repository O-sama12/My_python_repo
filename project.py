#Importing required package(s) 
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import tkinter.messagebox
#Creating the base
root = tkinter.Tk()
#App title
root.title("PCS Desktop App")
root.geometry('500x300')
label = Label(root, text = "Hi user, please click upload button to upload your file(s) in cloud storage")
label.pack()
button = Button(root, text="Upload", command=lambda:upload_file(), height=4, width=8)
def upload_file():
    file = filedialog.askopenfilename()
    fob = open(file, 'r')
    print(fob.read())
    label.config(text = "You've successfully saved your file. Feel free to close it")
closebutton = Button(root, text = "Close", command = root.destroy)
closebutton.pack(side = BOTTOM, padx = 15, pady = 20)
button.pack(side='bottom')
root.mainloop()
