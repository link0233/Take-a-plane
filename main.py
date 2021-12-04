from gugu.gugu_main import gugu
from main_screen.title import mainScreenTitle
from main_screen.startButton import *

class main(gugu):
    def __init__(self):
        super(main,self).__init__("射飛機","skyblue",640,480)
        self.mainScreenStart()#主畫面
        while True:
            self.mainScreenUpdate()
            self.update()

    def mainScreenStart(self):
        self.mainScreenTitle=mainScreenTitle(self)
        self.mainScreenStartButton=mainScreen_StartButton(self)

    def mainScreenUpdate(self):
        self.mainScreenStartButton.update()

if __name__=='__main__':
    main()