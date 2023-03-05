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
print(y)  # returns ['From: Using the :']

print()

# Non-greedy matching
import re

x = "From: Using the :character"
y = re.findall("^F.+?:", x)
print(y)  # returns ['From:']

print()

# Fine tuning string extraction
mail = "From fastoch@ik.me Sun Mar 5 11:17 2023"
x = re.findall("^From \S+@\S+", mail)  # \S+ = at least one non-whitespace character
print(x)
y = re.findall("^From (\S+@\S+)", mail) # line starts with 'From' and parentheses delimit the extraction
print(y) 
z = re.findall('\S+@\S+', mail)
print(z)

print()

# Extracting the domain name (after @)
mail = "From fastoch@ik.me Sun Mar 5 11:17 2023"
x = re.findall("@([^ ]+)", mail)  # look until you find an @ (at sign) and match any non-blank character
# ^ (caret sign) in between square brackets does not mean 'line starts with', it means 'not', in this case 'not blank'
print(x)

# extracting the username (before @)
y = re.findall("([^ ]+)@", mail)
print(y)