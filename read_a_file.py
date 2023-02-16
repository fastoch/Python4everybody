xfile = open('/home/fastoch/Documents/test.txt')
for line in xfile:
    print(line, end="") 
    # end="" cancels the automatic addition of a newline

print()

# Reading the whole file
xfile = open('/home/fastoch/Documents/test.txt')
inp = xfile.read()
print(len(inp)) # print the length of the file (number of characters)
print(inp[:25]) # print the 25 first characters in the file
