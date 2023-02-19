han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()    #  removes \n at the end of each line
    words = line.split()

    # first, we check the number of words on the line, and then we ensure the line starts with 'From'
    # in such a compound statement, if first condition is True, the second one is not checked, so the order matters
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])