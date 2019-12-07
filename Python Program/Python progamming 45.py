class Computer:
    def __init__(self):
        self.name="Navin"
        self.age=28

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age==other.age:
            print("They are same")
        else:
            print("They are different")

c1=Computer()
c2=Computer()
print(id(c1))
print(c1.name)

if c1.compare(c2):
    print("They are same")

c1.name="Chanuka"
print(c1.name)

c1.update()