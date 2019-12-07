from array import *

vals=array('i',[3,4,5,6,7,8,3])
print(vals)

print(vals.buffer_info())
print(vals.reverse())

for i in range(5):
    print(vals[i])

val=('u',['e','r','t'])
newArr=array(vals.typecode,(a*a for a in vals))
for e in newArr:
	print(e)
