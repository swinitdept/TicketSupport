# Import Stuff Here
from tkinter import *
import os

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()




    def init_window(self):
        self.master.title("Swin Ticket Support")
        self.pack(fill=BOTH, expand=1)

    ### BUTTONS ###


        # Title
        samepleTxt = Label(self, text="Swinomish Casino and Lodge Support Ticket")
        samepleTxt.pack()

        # Name field
        v = StringVar()
        samepleTxt = Label(self, text="Name:")
        samepleTxt.place(x=10,y=40)
        name_field = Entry(self)
        name_field.place(x=200, y=40)
        name_field.insert(0, os.getlogin())
        testVar = name_field
        print(testVar)

        # Department field
        samepleTxt = Label(self, text="Department:")
        samepleTxt.place(x=10,y=70)
        dept_field = Entry(self)
        dept_field.place(x=200, y=70)

        # Subject field
        samepleTxt = Label(self, text="Subject (optional):")
        samepleTxt.place(x=10,y=100)
        #samepleTxt.pack()
        subject_field = Entry(self)
        subject_field.place(x=200, y=100)

        # Problem(s) field
        samepleTxt = Label(self, text="Problem(s):")
        samepleTxt.place(x=10,y=130)
        problem_field = Entry(self)
        problem_field.place(x=200, y=130)


        quitButton = Button(self, text="Quit", command=self.client_exit, width=10, height=2, bg="red")
        quitButton.place(x=50, y=150)

        submitButton = Button(self, text="Submit", command=self.client_submit, width=10, height=2, bg="lightgreen")
        submitButton.place(x=50, y=250)

    def client_exit(self):
        exit()

    def client_submit(self):
        print(Window.name_field.get())
        #file = open("%s.txt" % os.getlogin(), "a")
        #file.write("Name: " + self.entry.get())

    #def showText(self):
        #text = Label(self, text="Hello")
        #text.pack()

root = Tk()
root.geometry("400x450")

app = Window(root)

root.mainloop()
