from gugu.gugu_main import gugu

class main(gugu):
    def __init__(self):
        super(main,self).__init__("射飛機","#000000",640,480)
        self.mainloopp()

if __name__=='__main__':
    main()