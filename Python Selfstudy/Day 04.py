num1 = int(input("Enter first value:"))
num2 = int(input("Enter second value:"))
Oper=str(input("Choose operation:"))
if Oper=="+":
    result=num1+num2
    print(result)
elif Oper=="-":
    result=num1-num2
    print(result)
elif Oper=="/":
    result=num1/num2
    print(result)
elif Oper=="*":
    result=num1*num2
    print(result)
elif Oper=="^":
    result=pow(num1,num2)
    print(result)
else:
    print("You cann't perform this operation in here.")

