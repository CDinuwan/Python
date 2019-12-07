class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        #This is a constructor
    def config(self):
        print("Config is",self.cpu,self.ram)
com1=Computer('i5',16)
com2=Computer('Ryzen3',8)

com1.config()
com2.config()
