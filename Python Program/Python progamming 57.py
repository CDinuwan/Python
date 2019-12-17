f=open('Mydata','r')

print(f.readline(),end="#")
print(f.readline())

print(f.readline(4))

f1=open('abc','w')
f1.write("Something")
f1.write("People")#In here we lost previous Data
f1=open('abc','a')

for data in f:
    print(data)

for data in f:
    f1.write(data)

f=open('IMG1.jpg','rb')

for i in f:
    print(i)

f1=open("Mypic.jpg","wb")

for i in f:
    f1.write(i)