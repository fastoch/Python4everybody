xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    print(line, end="") 
    # end="" deletes additional newlines at the end of each line
    # because the print() function adds a newline to those already existing in the file

print('\n'+'*'*64+'\n')

# same thing with rstrip() instead of using end=""
xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    line = line.rstrip() # each newline is considered a whitespace and therefore is stripped
    print(line) 

print('\n'+'*'*64+'\n') # separator

# Reading the whole file
xfile = open('/home/fastoch/Documents/test.txt')
inp = xfile.read()
print(len(inp)) # print the length of the file (number of characters)
print(inp[:25]) # print the 25 first characters in the file

print('\n'+'*'*64+'\n')

# skip a line with continue
xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    if not line.startswith('spirit'):
        continue
    print(line, end="")

print('\n'+'*'*64+'\n')

# using in to select lines 
xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    line = line.rstrip()
    if not 'brackets' in line:
        continue
    print(line)

print('\n'+'*'*64+'\n')

# prompt for file location
flocat = input('Enter the file location: ')
fhand = open(flocat)
count = 0
for line in fhand:
    if 'brackets' in line:
        count += 1
print('There were', count, 'lines containing \'brackets\' in', flocat)

print('\n'+'*'*64+'\n')

# Handling bad user input
flocat = input('Enter the file location: ')
try:
    fhand = open(flocat)
except: 
    print('File cannot be opened:', flocat)
    quit() # very important to prevent from executing the rest of the code

count = 0
for line in fhand:
    if 'brackets' in line:
        count += 1
print('There were', count, 'lines containing \'brackets\' in', flocat)

print('\n'+'*'*64+'\n')