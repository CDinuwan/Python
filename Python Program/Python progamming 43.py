class Computer:
    def config(self):
        print("i5,16gb,1TB")
a='a'
com1=Computer()
print(type(com1))

x=9
print(type(x))

Computer.config(com1)
com1.config()