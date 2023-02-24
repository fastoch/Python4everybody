fname = input('Enter file: ')
# if I just hit Enter, it will select clown.txt 
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

counts = dict()
for line in hand:
    line = line.rstrip() # remove whitespace from the right-hand side
    wds = line.split() # turn each line into a list of words
    for w in wds: # for each word in my file
        counts[w] = counts.get(w,0) + 1 # initialize counter | retrieve & update counter

print(counts)

# Now we want to find the most common word
biggest = 0
theWord = ''
for k,v in counts.items():  # items() returns key,value pairs as a list of tuples
    if v > biggest:
        biggest = v
        theWord = k
print('Most frequent word is *' + theWord + '*, which is repeated', biggest, 'times')
