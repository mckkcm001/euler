import tkinter

class Slideshow:
    def __init__(self, delay=20000):
        self.count = 0
        root = tkinter.Tk()
        root.geometry("1200x300")
        label1 = tkinter.Label(root,wraplength = 1150, justify='left')
        label2 = tkinter.Label(root)
        label1.pack()
        label2.pack(side = "bottom")
        self.label1 = label1
        self.label2 = label2
        self.root = root
        self.questions = [
'Directions \n\
Start a text document and Save As per#.10-2.joe666666.bob777777.sue888888 \n\
In the document, type this header: \n\
Name 1              Date \n\
Name 2 \n\
Name 3 \n\n\
10-2',
'Name of writer \n\
1.\tIn words and equation, state the first law of thermodynamics.\n\
\tIf Q is positive, is heat entering or leaving the system?\n\
\tIf W is positive, is work entering or leaving the system?',
'Name of writer \n\
2.\tThe internal energy of a gas decreases by 344 J.\n\
\tIf the process is adiabatic, how much energy is transferred as heat?\n\
\tHow much work is done on or by the gas? ',
'Name of writer \n\
3.\tHeat is added to a system, and the system does 26 J of work. \n\
\tIf the internal energy increases by 7 J, how much heat was added to the system?',
'Name of writer \n\
4.\tWhy is the net change in internal energy of a system zero for a cyclic process? \n\
\tWhat does this imply about the net heat and net work for the system?',
'Save, Close, Copy, Paste into turnin folder, logout, or shutdown']
        self.question = self.questions.pop(0)
        self.delay = delay 
        root.after(1, self.showQuestion)
        root.mainloop()

    def showQuestion(self):       
        self.label1.configure(text=self.question,font=("Helvetica", 16))
        self.label2.configure(text=str(self.count//1000),font=("Helvetica", 24))
        if self.count > self.delay:
            if len(self.questions) > 0:
                self.count = 0
                self.question = self.questions.pop(0)
                self.root.after(1000, self.showQuestion)
            else:
                self.root.after(1000, self.root.quit)
        else:
            self.count += 1000
            self.root.after(1000, self.showQuestion)
            
    def quit(self):
        self.root.quit()

if __name__ == "__main__":
    app=Slideshow(2000)
