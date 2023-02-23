purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] += 2
print(purse)

print('*'*64)

# Comparing lists and dictionaries
# Dictionaries are like lists except that they use keys instead of numbers to look up values
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

print('*'*64)

# One common use of dictionaries is counting how often we "see" something
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# The get method for dictionaries
if name in counts:
    x = counts[name]
else: 
    x = 0
# The 4 lines above are equivalent to this line:
x = counts.get(name, 0)

# Simplified counting with get()
# We can use get() and provide a default value of zero when the key is not yet in the dictionary, 
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    # if exists, increment it by 1
    # if new, set the count to 1
    counts[name] = counts.get(name, 0) + 1 
print(counts)

print('*'*64)

# Counting words in text - Counting Pattern
counts = dict()
line = input('Enter a line of text: ')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# Finding the most repeated word in a file
name = input('Enter file location: ')
handle = open(name)

counts = dict()
for line in handle: # for every line in my file
    words = line.split()
    for word in words: # for every word in every line
        counts[word] = counts.get(word, 0) + 1

bigCount = None 
bigWord = None
for word,count in counts.items(): # counts.items() returns key-value pairs of the dictionary, as tuples in a list
    if bigCount is None or count > bigCount:
        bigWord = word # most repeated word
        bigCount = count # number of repetitions

print(bigWord, bigCount)

