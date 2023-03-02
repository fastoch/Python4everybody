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
d = {'b':10, 'd':1, 'c':22, 'e':16, 'a':8}

# First, we sort the sort the dictionary by key using the items() method and sorted() function
print('Not sorted:', d.items())
keySorted = sorted(d.items())
print('Sorted by key:', keySorted)
for k,v in d.items():
    print(k, v)

print()

# Sorting by value instead of key
valuesFirst = list()
for k,v in d.items():
    valuesFirst.append((v,k))
print('(value, key) instead of (key, value):', valuesFirst)

valueSorted = sorted(valuesFirst)
print('Sorted by value:', valueSorted)

valueSortedReversed = sorted(valueSorted, reverse=True)
print('Sorted by value and reversed:', valueSortedReversed)

print()


# The top 10 most common words
fhand = open('romeo-full.txt') # open my file
counts = dict() # create a dictionary for storing each word's count
for line in fhand:
    words = line.split() # turn each line into a list of words
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # initialize or increment counting
# We transfer our dictionary entries into a list of tuples
lst = list() 
for key, val in counts.items():
    newTuple = (val, key) # value becomes first element of each tuple, so that we can later sort by value
    lst.append(newTuple)

lst = sorted(lst, reverse=True) # sorting our list by value and reversing the order so that biggest values come first
# We print out top 10 most common words and the corresponding count
for val, key in lst[:10]:
    print(key, val)

# The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
print()


# Top 10 most common words - SHORTER VERSION
fhand = open('romeo-full.txt') 
counts = dict() 
for line in fhand:
    words = line.split() # default separator = whitespace
    for word in words:
        counts[word] = counts.get(word, 0) + 1
reversedSortedTuple = sorted([(v,k) for k,v in counts.items()], reverse=True) # reverse=True is for sorting from highest value to lowest
for v,k in reversedSortedTuple[:10]:
    print(k,v)

