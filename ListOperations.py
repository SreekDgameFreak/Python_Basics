#An Item at a certain index can be re assigned.
numbers = [7,7,7,7,7,7]
numbers[3] = 2
print(numbers)

#Lists can be added and multiplied same way as strings
str = "Hello"
print(str+" suffixing")
print(str*3)
lst = [1,2,3,4,5]
print(lst+[6,7,8])
print(lst*3)

#To check if an item is in a list, 'in' keyword can be used
lst = [1,2,3,4,5,6,7,"Hello","World"]
print(4 in lst)
print(100 in lst)
print("Hello" in lst)
print("world" in lst)
