from tkinter import Tk,Canvas

class gugu(Canvas):
    def __init__(self,title,color,_width,_height):
        self.root=Tk()
        self.root.title(title)
        super(gugu,self).__init__(self.root,width=_width,height=_height,bg=color)
        self.pack()
        self.items={}
        self.items2=[]

    def update(self):
        self.root.update()
    
    def mainloopp(self):
        while True:
            self.update()

    def newRec(self,Position,color):
        return Rec(self,Position,color)

    def newText(self,position,_text,color,size):
        return Text(self,position,_text,color,size)
    
    def newLabel(self,position,text,bgcolor,color,size,width=0,height=0):
        return Label(self,position,text,bgcolor,color,size,width,height)
        

class Rec:
    def __init__(self,gugu,Position,color):
        self.gugu=gugu
        self.item=self.gugu.create_rectangle(Position[0],Position[1],Position[2],Position[3],fill=color)

    def delete(self):
        self.gugu.delete(self.item)
    
    def update(self):
        print('ok')

class Text:
    def __init__(self,gugu,position,_text,color,size):
        self.gugu=gugu
        self.item=self.gugu.create_text(position[0],position[1],text=_text,fill=color,font=('Arial',size))

    def delete(self):
        self.gugu.delete(self.item)
        
    def update(self):
        print('ok')

class Label:
    def __init__(self,gugu,position,text,bgcolor,color,size,width=0,height=0):
        self.gugu=gugu
        if bgcolor!=None:
            self.position=[position[0]-width,position[1]-height,position[0]+width,position[1]+height]
            self.kkk=self.gugu.newRec(self.position,bgcolor)
        else:
            self.kkk=None
        self.kkkd=self.gugu.newText(position,text,color,size)

    def update(self):
        if self.kkk!=None:
            self.kkk.update()
        self.kkkd.update()