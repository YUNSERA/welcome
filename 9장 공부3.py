from tkinter import*

class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("레이블 변경하기 데모")
        
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "프로그래밍은 재미있습니다.")
        self.lbl.pack()
        
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2,text = "텍스트를 입력하세요.")
        
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2,text="텍스트를 변경한다.", command = self.processButton)
        
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2,text = "red", bg = "red", variable = self.v1, value ='R',command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2,text="yellow",bg ="yellow",variable = self.v1,value = 'Y',command = self.processRadiobutton)
        
        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)
        
        window.mainloop()
        
    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
            
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "yellow"
    
    def processButton(self):
        self.lbl["text"] = self.msg.get()

c1 = ChangeLabelDemo()