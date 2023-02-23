fname = input('Enter file: ')
# if I just hit Enter, it will select clown.txt 
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

for line in hand:
    line = line.rstrip() # remove whitespace off the right-hand side
    print(line)

