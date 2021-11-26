from tkinter import Tk,Canvas

class gugu(Canvas):
    def __init__(self,title,color,_width,_height):
        self.root=Tk()
        self.root.title(title)
        super(gugu,self).__init__(self.root,width=_width,height=_height,bg=color)
        self.pack()
    
    def mainloopp(self):
        self.root.mainloop()