from tkinter import Tk,Canvas

class gugu(Canvas):
    def __init__(self,title,color,_width,_height):
        self.root=Tk()
        self.root.title(title)
        super(gugu,self).__init__(self.root,width=_width,height=_height,bg=color)
        self.pack()
        self.items={}
        self.items2=[]
        self.key={
            'Position':[0,0],
            'Button1':0
        }
        self.keyStart()

    def keyStart(self):
        self.bind('<Button-1>',self.keyButton1)
        self.bind('<Motion>',self.motion)

    def motion(self,event):
        self.key['Position']=[event.x,event.y]

    def keyButton1(self,event):
        self.key['Button1']=1
        self.key['Position']=[event.x,event.y]

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

    def newButton(self,position,text,bgcolor,textcolor,bgcolor2,textsize):
        return button(self,position,text,bgcolor,textcolor,bgcolor2,textsize)
        

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

class button:
    def __init__(self,guguu,position,text,bgcolor,textcolor,bgcolor2,textsize):
        self.gugu=guguu
        self.create(position,text,bgcolor,textcolor,bgcolor2,textsize,1)

    def create(self,position,text,bgcolor,textcolor,bgcolor2,textsize,type):
        self.textposition=[(position[0]+position[2])//2,(position[1]+position[3])//2]
        if type==1:
            self.bg=gugu.newRec(self.gugu,position,bgcolor)
        else:
            self.bg=gugu.newRec(self.gugu,position,bgcolor2)
        self.text=gugu.newText(self.gugu,self.textposition,text,textcolor,textsize)
        self.item={
            'position':position,
            'text':text,
            'bgcolor':bgcolor,
            'bgcolor2':bgcolor2,
            'textcolor':textcolor,
            'textsize':textsize
        }

    def update(self,gugu_key):
        self.mousePosition=gugu_key.mouse    