han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()    #  removes \n at the end of each line
    words = line.split()
    if len(words) < 1:      # ignores blank lines
        continue
    if words[0] != 'From':  # ignores lines that do not start with 'From'
        continue
    print(words[2])