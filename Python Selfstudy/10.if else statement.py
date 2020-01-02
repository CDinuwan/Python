is_Male = True
is_tall = True
if is_Male or is_tall:
    print("You are Male and tall") 
elif is_Male and not(is_tall):
    print("You are short male")
elif not(is_Male) and is_tall:
    print("You are not a Male but you are tall")
else:
    print("You are not a Male")


def max_num(num1,num2,num3):
    if num1>=num2 and num1 >=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(60,63,87))
