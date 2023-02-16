stuff = 'Hello World!'

lowerCase = stuff.lower()
print(lowerCase)
print()

upperCase = stuff.upper()
print(upperCase)
print()

print(type(stuff))
print()

# list all methods that can be applied to my string
print(dir(stuff))
print()

# Search & Replace
greet = 'Hello Bob!'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)
print()

# Stripping whitespaces
greet2 = '   Hello Bob   '
print(greet2+'!')
print(greet2.lstrip()+'!')
print(greet2.rstrip()+'!')
print(greet2.strip()+'!')
print()

line = 'Please, have a nice day!'
print(line.startswith('Please')) # returns True
print(line.startswith('Hello')) # returns False
print()
