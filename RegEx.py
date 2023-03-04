# Using re.search() like find()

# using find()
hand = open("mbox-short.txt")
count = 0
for line in hand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
        count += 1
print("Number of lines containing 'From':", count)

print()

# using re.search()
import re

hand = open("mbox-short.txt")
count = 0
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
        count += 1
print("Number of lines containing 'From':", count)
