from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        label = Label(window,text = "welcome to python.")
        button_OK = Button(window, fg ="red", bg = "white",text ="OK",command = self.processOK)
        button_Cancle = Button(window,text ="Cancle",command = self.processCancle)
        
        label.pack()
        button_OK.pack()
        button_Cancle.pack()
        
        window.mainloop()
        
    def processOK(self):
        print("OK버튼 눌림")
    
    def processCancle(self):
        print("Cancle버튼 눌림")
        
ProcessButtonEvent()

