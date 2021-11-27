from tkinter import Tk,Canvas

class gugu(Canvas):
    def __init__(self,title,color,_width,_height):
        self.root=Tk()
        self.root.title(title)
        super(gugu,self).__init__(self.root,width=_width,height=_height,bg=color)
        self.pack()
    
    def mainloopp(self):
        self.root.mainloop()

    def newRec(self,Position,color):
        return self.create_rectangle(Position[0],Position[1],Position[2],Position[3],fill=color)

    def newText(self,position,_text,color,size):
        return self.create_text(position[0],position[1],text=_text,fill=color,font=('Arial',size))
    
    def newLabel(self,position,text,bgcolor,color,size,width=0,height=0):
        if bgcolor!=None:
            self.position=[position[0]-width,position[1]-height,position[0]+width,position[1]+height]
            self.newRec(self.position,bgcolor)
        self.newText(position,text,color,size)