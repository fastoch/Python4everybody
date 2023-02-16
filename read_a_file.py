xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    print(line, end="") 
    # end="" deletes additional newlines at the end of each line
    # because the print() function adds a newline to those already existing in the file

print()

# alternative to using end=""
xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    line = line.rstrip() # each newline is considered a whitespace and therefore is stripped
    print(line) 

print()

# Reading the whole file
xfile = open('/home/fastoch/Documents/test.txt')
inp = xfile.read()
print(len(inp)) # print the length of the file (number of characters)
print(inp[:25]) # print the 25 first characters in the file

print()
