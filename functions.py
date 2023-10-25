#functions in python
#string  transform functions
#capitalize
message = "hi, how are you?"
print(message.capitalize())

#title
name = "prasad aketi25"
print(name.title())

#upper
name = "prasad aketi25"
print(name.upper())

#lower
name = "PRASAD AKETI25"
print(name.lower())

#casefold
name = "PRASAD AKETI@25"
print(name.casefold())

#swapcase
name = "PRASAD AKETI25"
print(name.swapcase())

name = "prasad aketi25"
print(name.swapcase())

#string check functions

#isnumeric
a = "12234"
print(a.isnumeric())

#isalnum
a = "prasad25"
print(a.isalnum())
b = "prasad"
print(b.isalnum())

#isdigit
a = "235"
print(a.isdigit())

#isasscii
a = "G4G"
print(a.isascii())

#isupper
a = "PRASAD AKETI"
print(a.isupper())

#islower
a = "prasadaketi"
print(a.islower())

#isspace
a = " "
print(a.isspace())

b = "prasad"
print(b.isspace())

#isidentifier
a = "prasad_aketi25"
print(a.isidentifier())

#isprintable
a = "prasad_aketi6342"
print(a.isprintable())

#istitle
a = "Hello, Welcome!"
print(a.istitle())

#string len function
name = "prasad aketi25"
print(len(name))

#string search functions

#index
email = "prasad25@gmail.com"
print(email.index("2"))
print(email.index("@"))

#rindex
email = "prasad@25@gmail.com"
print(email.rindex("5"))
print(email.rindex("@"))

#find
email = "prasad25@gmail.com"
print(email.find("3"))
print(email.find("b"))

email = "prasad25@gmail.com"
print(email.find("2"))
print(email.find("@"))

#rfind
email = "prasad@25@gmail.com"
print(email.rfind("2"))
print(email.rfind("@"))

#startswith
email = "prasad25@gmail.com"
print(email.startswith("prasad"))
print(email.startswith("25"))

#endswith
email = "prasad25@gmail.com"
print(email.endswith("prasad"))
print(email.endswith(".com"))

#CRUD functions
#create/add data
#append
lst = []
lst.append("prasad")
lst.append("25")
print(lst)

#insert
names = ["a", "b", "c"]
names.insert(2, "prasad")
print(names)

#read
names = ["a", "b", "c"]
print(names.index("b"))

#count
names = ["a", "b", "c", "a"]
print(names.count("a"))

#extend
names = ["a", "b", "c"]
num = ["1", "2", "3"]
names.extend(num)
print(names)

#remove
names = ["prasad", "aketi", "25"]
names.remove("aketi")
print(names)

#pop with index
names = ["prasad", "aketi", "25"]
names.pop(2)
print(names)

#pop without index
names = ["prasad", "aketi", "25"]
names.pop()
names.pop()
print(names)

#clear
names = ["prasad", "aketi", "25"]
names.clear()
print(names)

#sort
num = [8, 3, 5, 2, 6, 1]
num.sort()
print(num)

#reverse
num = [8, 3, 5, 2, 6, 1]
num.reverse()
print(num)