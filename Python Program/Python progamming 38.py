
from functools import reduce

def update(n):
    return n+2
nums=[3,2,5,8,9,6,4,65]


def add_all(a,b):
    return a+b
evens=list(filter(lambda n:n%2==0,nums))

doubles =list(map(lambda n:n*2,evens))

sum=reduce(lambda a,b:a+b,doubles)

print(sum)
print(evens)

