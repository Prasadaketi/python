# string slicing

name = "prasad"
print(name[1:4])
print(name[:])
print(name[2:])
print(name[:5])
# negative index

print(name[-6:-2])
print(name[-4:])
print(name[:-1])


# reverse a string
name = "prasadaketi25"
str = (name[::-1])
print(str)

# reverse a string a without slicing
name = "prasadaketi25"
str = "".join(reversed(name))
print(str)

# reverse a  list items
names = list(("prasad", "deva", "priyam"))
print(names[::-1])
