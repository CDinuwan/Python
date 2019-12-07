from array import *

arr= array('i',[])
n =int(input("Enter the length of the array:"))
for i in range(n):
    x=int(input("Enter the next value:"))
    arr.append(x)
print(arr)

val=int(input("Enter the value:"))

k=0
for i in arr:
    if i==val:
        print(k)
        break
    k+=1