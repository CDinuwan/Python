def fib(n):
    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):#n=10
        c=a+b
        a=b
        b=c
        print(c)
fib(5)