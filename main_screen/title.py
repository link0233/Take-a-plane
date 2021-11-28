class mainScreenTitle:
    def __init__(self,gugu):
        self.gugu=gugu
        self.item=self.gugu.newLabel((320,100),"射飛機",'#ff0000','#ffffff',50,width=100,height=50)
        self.item.update()