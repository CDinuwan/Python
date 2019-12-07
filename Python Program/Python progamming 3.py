nums=[25,12,35,96,14]
print(nums)
print(nums[0])
print(nums[4])
print(nums[2:])
print(nums[-5])
names=['navin','kiran','jhone']
values=[24,'kiran',90.9]

#Use this for add values End of the list
nums.append(45)
print(nums)

#insert can add values to any place in list
nums.insert(2,33)
print(nums)

#remove use to delete a value in function.
nums.remove(33)
print(nums)

nums.pop()
print(nums)

nums.pop(2)
print(nums)

del nums[2:]
print(nums)

nums.extend([33,45,66,75,84])
print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))