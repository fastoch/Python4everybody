fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

print()

# same thing with a for loop (iteration variable is implicit)
fruit = "pineapple"
for letter in fruit:
    print(letter)

print()

# count the number of times the loop encounters the 'a' character
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)