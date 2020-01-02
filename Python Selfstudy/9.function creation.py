#Tuples

cordinates=(4,6)
print(cordinates[1])

tuples=[(4,6),(8,9),(5,0)]
tuples[1]=10
print(tuples[1])

#Function

def sayhi():
    print("Hi, Hello")

print("Top")
sayhi()
print("Bottom")

def say_hi(name,age):
    print("Hello User "+ name +"Your age "+ str(age))

say_hi("Chanuka",25)

def cube(num):
    return num*num*num

print(cube(4))
