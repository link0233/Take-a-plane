class mainScreen_StartButton:
    def __init__(self,gugu):
        self.gugu=gugu
        self.item=self.gugu.newButton([20,20,100,50],'hello','#ffffff','#000000','#00ff00',13,self.dk)

    def update(self):
        self.item.update(self.gugu.key)

    def dk(self):
        print(00)