n=float(input("Enetr Your Value:"))
n1=float(input("Enetr Your Second Value:"))
op=input("Enter Operator:")

if op=="+":
    print(n+n1)
elif op=="-":
    print(n-n1)
elif op=="*":
    print(n*n1)
elif op=="/":
    print(n/n1)
else:
    print("invalid Operator")