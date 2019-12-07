def person(name, **data):
	print(name)
	print(data)

    for i,j in data.items():
        print(i,j)

person('chanuka',age=25,city='mumbai',mob=23131323)

