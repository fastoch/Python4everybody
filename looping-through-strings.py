fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

print()

# same thing with a for loop
fruit = "pineapple"
index = 0
for letter in fruit:
    print(index, letter)
    index += 1