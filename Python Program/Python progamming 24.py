from numpy import *

arr=array([1,2,3,4,5])
print(arr)

print(arr.dtype)

arr=array([1,2,3,4,5],float)
print(arr)

arr=linspace(0,16,10)
print(arr)

arr=arange(1,25,2)

arr=logspace(1,20,5)
print('%.2f'%arr[4])#To remove e

arr=ones(5)
print(arr)

arr=zeros(5)
print(arr)