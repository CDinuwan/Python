#Exception Handling
#Compile,Logical,Runtime Error

a=5
b=0

k=int(input("Enter a number:"))

try:
    print(a/b)
except Exception as e:
    print("Hey,You cant divide a number by 0",e)

except ValueError as e:
    print("Invalid Input")
finally:print("Resourse Closed")

