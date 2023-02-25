tup = ('Timothée', 'Sandro', 'Aurélie', 'Fabrice')
print(tup)
print(tup[2])

y = (1, 6 , 8, 2)
print(y)
print(max(y))

l = list()
print('Methods you can use with a list:')
print(dir(l))

print()

t = tuple()
print('Methods you can use with a tuple:')
print(dir(t))

print()

# Tuples & Assignment
(x, y) = (4, 'Fred')
print(y)

print()

# Tuples & Dictionaries
d = dict()
d['fastoch'] = 82
d['Sandro'] = 16
for k,v in d.items():
    print(k, v)
print()
# The items() method in dictionaries returns a list of (key,value) tuples
tups = d.items()
print(tups)
