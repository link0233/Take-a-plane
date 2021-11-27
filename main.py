from gugu.gugu_main import gugu

class main(gugu):
    def __init__(self):
        super(main,self).__init__("射飛機","skyblue",640,480)
        self.newLabel((50,100),"hello",None,'#ffffff',12,width=25,height=30)
        self.mainloopp()

if __name__=='__main__':
    main()