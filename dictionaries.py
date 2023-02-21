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
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

print('*'*64)

