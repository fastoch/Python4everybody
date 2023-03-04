# Using re.search() like find()

# using find()
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)

print()

# using re.search()
import re

hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
