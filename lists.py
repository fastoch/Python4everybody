# lists are the simplest data structures
# a list is a type of collection
friends = ['Sandro','Aurélie','Timothée']
for friend in friends:
    print('Happy Birthday',friend)
print('Done!')

# Concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # will print [1,2,3,4,5,6]

# List can be sliced using :
t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
# just like in strings, the second number is "up to but not including"

# List Methods
x = list() # creates an empty list
print(x)
print(type(x))
print(dir(x)) # list all methods available for my list

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# is something in a list?
some = ['Sandro',26,32,'Timothée',16]
print(32 in some)
print('Aurélie' not in some)
print('Sandro' in some)
print(16 not in some)

# Lists are sortable
friends = ['Rachel','Ross','Monica','Chandler','Joey','Phoebe']
friends.sort()
print(friends)
