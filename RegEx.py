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

print()

# From matching to extracting data
import re

x = "My 2 favorite numbers are 16 and 82"
y = re.findall("[0-9]+", x)
print(y)
z = re.findall("[aeiou]+", x)
print(z)
a = re.findall("[AEIOU]+", x)
print(a)

print()

# Greedy matching
import re

x = "From: Using the :character"
y = re.findall("^F.+:", x)
print(y)

print()

# Non-greedy matching
import re

x = "From: Using the :character"
y = re.findall("^F.+?:", x)
print(y)

print()
