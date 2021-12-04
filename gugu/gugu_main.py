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
        self.key['Button1']=0
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

    def newButton(self,position,text,bgcolor,textcolor,bgcolor2,textsize,comment):
        return button(self,position,text,bgcolor,textcolor,bgcolor2,textsize,comment)
        

class Rec:
    def __init__(self,gugu,Position,color):
        self.gugu=gugu
        self.item=self.gugu.create_rectangle(Position[0],Position[1],Position[2],Position[3],fill=color)

    def delete(self):
        self.gugu.delete(self.item)
        self.item=None
    
    def update(self):
        pass

class Text:
    def __init__(self,gugu,position,_text,color,size):
        self.gugu=gugu
        self.item=self.gugu.create_text(position[0],position[1],text=_text,fill=color,font=('Arial',size))

    def delete(self):
        self.gugu.delete(self.item)
        self.item=None
        
    def update(self):
        pass

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
    def __init__(self,guguu,position,text,bgcolor,textcolor,bgcolor2,textsize,comment):
        self.gugu=guguu
        self.item={
            'position':position,
            'text':text,
            'bgcolor':bgcolor,
            'bgcolor2':bgcolor2,
            'textcolor':textcolor,
            'textsize':textsize
        }
        self.create(1)
        self.comment=comment

    def create(self,type):
        self.textposition=[(self.item['position'][0]+self.item['position'][2])//2,(self.item['position'][1]+self.item['position'][3])//2]
        if type==1:
            self.bg=gugu.newRec(self.gugu,self.item['position'],self.item['bgcolor'])
        else:
            self.bg=gugu.newRec(self.gugu,self.item['position'],self.item['bgcolor2'])
        self.text=gugu.newText(self.gugu,self.textposition,self.item['text'],self.item['textcolor'],self.item['textsize'])

    def update(self,gugu_key):
        self.mouse_connet(gugu_key)
    
    def mouse_connet(self,key):
        self.mousePosition=key['Position']
        self.Position=self.item['position']
        if self.mousePosition[0]>self.Position[0] and self.mousePosition[0]<self.Position[2] and self.mousePosition[1]>self.Position[1] and self.mousePosition[1]<self.Position[3]:
            self.delete()
            self.create(2)
            if key['Button1'] == 1:
                self.comment()
        else:
            self.delete()
            self.create(1)

    def delete(self):
        self.bg.delete()
        self.text.delete()
        self.bg=None
        self.text=None