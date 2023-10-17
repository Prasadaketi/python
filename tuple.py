# clear
names = ["a", "b", "c", "d"]
print(names.clear())
print(type(names))
print(names)

#delete
names = ["1", "a", "2", "b"]
del names[1]
print(names)
del(names)

#sort
num = ["2", "5", "6", "3", "4", "2", ]
num.sort()
print(num)

#reverse
num = ["2", "5", "6", "3", "4", "2", ]
num.reverse()
print(num)

#tuple
#count
tpl : tuple = (2, 5, 6, 3, 4, 2, 1, 2)
print(tpl.count(2))

#index
tpl : tuple = (2, 5, 6, 3, 4, 2, 1, 2)
print(tpl.index(1))

#tuple to list conversion
tpl : tuple = (2, 5, 6, 3, 4, 2, 1, 2)
lst = list(tpl)
print(type(lst))

#

