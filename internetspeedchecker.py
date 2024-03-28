from tkinter import *
from tkinter import messagebox
import pyspeedtest

def check_speed():
    speed = pyspeedtest.SpeedTest("www.google.com")
    download_speed = str(speed.download()) + " [Bytes Per Second]"
    messagebox.showinfo("Download Speed", download_speed)

root = Tk()
root.title("Internet Speed Checker")
root.config(bg="white")
root.geometry("500x250")

label1 = Label(root, text="Internet Speed Checker", font=("Arial", 30, "bold"), bg="blue")
label1.pack()

button1 = Button(root, text="Check Speed", font=("Arial", 20, "bold"), bg="yellow", height=1, width=10, command=check_speed)
button1.pack()

root.mainloop()
