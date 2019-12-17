pos=-1

def search(list,n):
    i=0

    while i<len(arr):
        if arr[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

arr=[5,8,6,7,8,9]
n=9

if search(list,n):
    print("Found",pos+1)
else:
    print("Not Found")