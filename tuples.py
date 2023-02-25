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

print()

# Sorting lists of tuples
d = {'a':10, 'b':1, 'c':22, 'd':16, 'e':8}
# First, we sort the sort the dictionary by key using the items() method and sorted() function
keySorted = sorted(d.items())
print('Sorted by key:', keySorted)
# NB: the sorted() function does not seem necessary, as the items() method already returns a sorted list of tuples
for k,v in d.items():
    print(k, v)

print()

# Sorting by value instead of key
valueSorted = list()
for k,v in d.items():
    valueSorted.append((v,k))
print('(value, key) instead of (key, value):', valueSorted)
valueSorted = sorted(valueSorted)
print('Sorted by value:', valueSorted)
valueSorted = sorted(valueSorted, reverse=True)
print('Sorted by value and reversed:', valueSorted)

