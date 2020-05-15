# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

from tkinter import *


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self, bg="white")

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        frame = Frame(self,)
        frame.pack(side="left",padx="100", pady="50")
        button = Button(frame, text="Visit Page 1", height=10, width=20,bg="green",fg="white",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(pady="30")

        button2 = Button(frame, text="Visit Page 2",height=10, width=20,bg="purple",fg="white",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady="30")
        frame1 = Frame(self,)
        frame1.pack(side="left",padx="100", pady="50")
        button = Button(frame1, text="Visit Page 1", height=10, width=20,bg="brown",fg="white",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(pady="30")

        button2 = Button(frame1, text="Visit Page 2", height=10, width=20,bg="blue",fg="white",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady="30")


class PageOne(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()