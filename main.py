from tkinter import *
from math import sqrt


class Calculator():
    def __init__(self,master):
        self.root = master
        self.root.geometry("1200x700")
        self.root.maxsize(485,590)
        self.root.title("Caculator")
        self.root.iconbitmap("cal-icon.ico")
        self.scvalue = StringVar()
        self.screen = Entry(self.root,textvariable=self.scvalue,font="comic 25",borderwidth=30,relief="sunken",background="lightblue",state="readonly").pack(anchor="nw",ipadx=27,padx=4)
        self.buttonsFrame = Frame(self.root)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="CE",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=29,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="C",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=30,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="√",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=30,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="+",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=30,ipady=10,padx=2,pady=5)
        
        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="7",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="8",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="9",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="-",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=34,ipady=10,padx=2,pady=5)

        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="4",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="5",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="6",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="x",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="1",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="2",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)


        self.b1 = Button(self.buttonFrameRow1,text="3",font="comic 25",background="lightblue")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="÷",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=35,ipady=10,padx=2,pady=5)

        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)

        self.b1 = Button(self.buttonFrameRow1,text="0",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=44,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text=".",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=38,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="%",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=26,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="=",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=30,ipady=10,padx=2,pady=5)
        self.buttonFrameRow1.pack(anchor="nw")

        self.buttonsFrame.pack(anchor="nw",padx=3)
    def calculate(self,event):
        self.text = event.widget.cget("text")
        if (self.text == "="):
            self.value = self.scvalue.get()
            self.value = self.value.replace("x","*")
            self.value = self.value.replace("÷","/")
            if "√" in self.scvalue.get():
                if self.scvalue.get().split("√")[0] != "":
                    self.squareRoot = sqrt(int("".join(self.scvalue.get().split("√")[1:])))
                    self.scvalue.set(self.squareRoot * int(self.scvalue.get().split("√")[0]))
                else:
                    self.squareRoot = sqrt(int("".join(self.scvalue.get().split("√")[1:])))
                    self.scvalue.set(self.squareRoot)
            else:
                self.result = eval(self.value)
                self.scvalue.set(self.result)

        elif(self.text == "CE"):
            self.scvalue.set(self.scvalue.get()[0:-1])

        elif (self.text == "C"):
            self.scvalue.set("")
        else:
            self.scvalue.set(self.scvalue.get() + self.text)

if __name__ == "__main__":     
    root = Tk()
           
    calculator = Calculator(root)

    root.mainloop()