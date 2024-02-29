fhand = open('mbox.txt')
for line in fhand:
    if not line.startswith('From') : continue # ignore lines not starting with 'From'
    if 'Jan' in line:
        words = line.split()
        print(words[1])