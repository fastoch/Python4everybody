fname = input('Enter file: ')
# if I just hit Enter, it will select clown.txt 
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

counts = dict()
for line in hand:
    line = line.rstrip() # remove whitespace from the right-hand side
    wds = line.split() # turn each line into a list of words
    for w in wds: # for each word in my file
        counts[w] = counts.get(w,0) + 1 
print(counts)