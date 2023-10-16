#list crud operations

#create/add data to a list

#append
name : list = []
name.append("prasad" "25")
print(name)

#insert
names = ["a", "b", "c"]
names.insert(1, "d")
print(names)

#Read items from list
names = ["a", "b", "c", "d"]
print(names.index("c"))

names = ["a", "b", "c", "d", "b", "a", "a"]
print(names.count("prasad"))
print(names.count("b"))
print(names.count("a"))

#Update items in a list
#by using index
names = ["a", "b", "c"]
names[1] = "prasad"
print(names)

#extend items in a list
names = ["a", "b", "c", "d"]
numbers = ["1", "2", "3", "4"]
names.extend(numbers)
print(names)
print(numbers)

#delete
#remove
names = ["abc", "123", "xyz"]
names.remove("123")
print(names)

#pop with index
names = ["abc", "123", "xyz"]
names.pop(2)
print(names)

#pop without index
names = ["abc", "123", "xyz"]
names.pop()
names.pop()
print(names)