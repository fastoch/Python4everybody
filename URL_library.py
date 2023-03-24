# This is a simplified version of the code written in 'basic_web_browser.py'
# 4 lines instead of 11

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

print()

counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand: 
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# the following block is for printing word-number pairs in descending order

liste = list()                          # preparing a list to register our dictionary entries as a list of tuples (a list can be sorted)
for word, number in counts.items():     # for each entry in our dictionary...
    entry = (number, word)              # ...create a tuple which first element = number of times a word appears
    liste.append(entry)                 # add this tuple to our list
liste = sorted(liste, reverse=True)     # sort our list by most frequent word 
for number,word in liste:
    print(word, number)
    
# The items() method returns a view object which contains the key-value pairs of the dictionary, as tuples in a list.