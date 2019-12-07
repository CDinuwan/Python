a=10
b=20
a=b
print(id(a))
print(id(b))
k=10
print(id(k))
print(type(a))
print(type(b))

#'a' value go to the garbage collection.
k=a
print(id(k))
b=8

