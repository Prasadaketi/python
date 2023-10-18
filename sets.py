#set data type
#implicit
a = {'a', '1', 'b', '2'}
print(a)

#explicit
b = set(('a', '1', 'b', '2'))
print(b)
print(type(b))

#data type/variable annotation
c: set = {'a', '2', 'b', '5'}
print(c)
print(type(c))

#create
#add
a:set = {'a', 'b', 'c'}
a.add('2')
print(a)

#read
#update
a = set(('a', 'b', 'c', 'd'))
b = set(('1', '2', '3', 'b'))
a.update(b)
print(a)

#delete
#remove
a = {'a', 'b', 'c', '1'}
a.remove('b')
print(a)

#discard
a = {'a', 'b', 'c', '1'}
a.discard('2')
print(a)

#pop
a = {'a', 'b', 'c', '1'}
a.pop()
print(a)

#union
a = set(('a', 'b', 'c', 'd'))
b = set(('1', '2', '3', 'b'))
print(a.union(b))

#intersection
a = set(('a', 'b', 'c', 'd'))
b = set(('1', '2', '3', 'b', 'a'))
print(a.intersection(b))
