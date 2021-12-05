class mainScreenQuitButton:
    def __init__(self,gugu):
        self.canvas=gugu
        self.item=self.canvas.newButton([530,420,630,470],'退出遊戲','#ffffff','#000000','#0f10ff',15,self.dk)

    def update(self):
        self.item.update(self.canvas.key)

    def dk(self):
        from sys import exit
        exit()