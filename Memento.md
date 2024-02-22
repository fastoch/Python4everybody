Timeline: from 0 to 205 min

## Reserved words: 
False, True, None, and, as, assert, break, continue, class, if, nonlocal,
def, del, elif, else, except, return, for, from, global, try, with, yield,
import, in, is, lambda, while, not, or, pass, raise, finally,

---

## Indentation
In your text editor, **turn tabs into 4 spaces**
In python, **indentation** is key. 
Increase/maintain after if or for.
Decrease to indicate end of block.

---

## Comments 
In Python, you can comment out a line by adding a pawn sign # before it.

---

## Conditional structure
```py
if :  
    instructions  
elif :  
    instructions  
else :  
    instructions
```

You can have no else.

---

## try & except
Surround a dangerous section of code with a try & except.  
If the code in the try works, then the except is skipped.  
If the code in the try fails, it jumps to the except section.  
The except block is only triggered when something goes wrong.
```py
var = input("Enter a number: ")
try:
    int(var) # fails if the input is not a number
    print("The number you entered is "+var) # executed only if you enter a number
except:
    print("Not a number!") # executed if you don't enter a number
```

---

## Functions (chapter 4)

Keep your code DRY (Don't Repeat Yourself) by using functions.
```py
def thing():
    print('Hello')
    name = input('What\'s your name? ')
    print('Nice to meet you '+ name + '!')

thing() # calling (or invoking) the function
```

A **function** is some reusable code that can take arguments as input, does some computation, 
and then **returns** a result or results.

An **argument** is a value we pass into the function as its input when we call the function.

A **parameter** is a variable which we use in the function definition. It is a "handle" that 
allows the code in the function to access the arguments for a particular function invocation.

There are 2 kinds of functions:
- **Built-in functions**: print(), input(), type(), float(), int(), string(), etc.
- **Functions that we define ourselves** and then use.

We treat the built-in function names as **reserved words**.

A "**fruitful**" function is one that produces a result (or return value).
The **return** statement ends the function execution and sends back a result.

**Void** (non-fruitful) functions do not return a value.

- We can define more than one **parameter** in the function definition.
- We simply add more **arguments** when we call the function.
- We must match the number and order of arguments with the parameters.
- We can declare some parameters as **optional**.

---

## Type conversions

- When you put an integer and floating point in an expression, the integer is **implicitly** 
converted to a float.
- You can control this with built-in functions int() and float().
- You can also use int() and float() to convert strings which contain numeric characters.

---

## Chapter 5 - Loops & iteration

Loops have iteration variables that change each time through a loop.
```py
n = 10
while n > 0 :
    print(n)
    n = n-1
print('Blastoff!')
print(n)
```

The **break** statement ends the current loop and jumps to the statement immediately
following the loop. It's like a loop test that can happen anywhere in the body of the loop.
```py
while True :
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
```

The **continue** statement ends the current iteration and jumps to the top of the loop to start
the next iteration.
```py
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!') 
```

While loops are called **indefinite loops** because they keep going until a logical condition becomes False.

### Definite Loops (for)

We can write a loop to run it once for each of the items in a set using the Python **for** construct.
We say that **definite loops** iterate through the members of a set.
```py
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
```

```py
friends = ['Monica','Rachel','Ross','Joey','Chandler','Phoebe']
for friend in friends:
    print('I\'ll be there for you', friend)
print('\'cause you\'re there for me too')
```

### Loop Idioms

#### What is the largest|smallest number?

```py
max = None
for i in [-20,-80,-10,-65,32]:
    if max is None:
        max = i
    elif i > max:
        max = i
print("The largest number in the list is: ", max)

# Smallest number
min = None
for j in [64,-128,2,0,-16]:
    if min is None:
        min = j
    elif j < min:
        min = j
print('The smallest number in the list is: ', min)
```

#### Counting in a loop

```py
counter = 0
print('Before', counter)
for i in [4, 16, -29, 32]:
    counter+=1
    print(counter, i)
print('After', counter)
```

#### Summing in a loop

```py
total = 0
print('Before', total)
for i in [4, 16, -29, 32]:
    total+=i
    print(total, i)
print('After', total)
```

#### Finding the Average in a loop

```py
counter = 0
total = 0
print('Counter:', counter, 'Total:', total)
for i in [4, 16, -29, 32]:
    counter+=1
    total+=i
    print('Counter:', counter, 'added value:', i, 'Total:', total)
average = total/counter
print('Counter:', counter, 'Total:', total, 'Average:', average)
```

#### Filtering in a loop

```py
counter = 0
total = 0
for value in [7, 36, 42, 1, 16, 33, 64]:
    if value > 30:
        print('Greater than 30',value)
        counter+=1
    total +=1
print(counter, 'values', 'out of', total, 'are greater than 30')
```

#### Search using a boolean variable

```py
found = False
print('Is there a Sandro in that list?')
for name in ['Sandro', 'Aurélie', 'Timothée', 'Fabrice']:
    if name == 'Sandro':
        found = True
if found == True:
    print('Yes there is.')
else:
    print('No there\'s no Sandro in that list.') 
```

### The "is" and "is not" operators

Python has an **is** operator that can be used in logical expressions.
It means "**is the same as**".  
It's similar to, but **stronger than ==**.  
**is not** is also a logical operator.  

For example:   
0 == 0.0 is True  
0 is 0.0 is False  
0 is not 0.0 is True

Use "is" **sparingly**. Only use it on **booleans** and on **None**.

---

## Chapter 6 - String Data Type

- A string is a sequence of characters.  
- A string literal uses quotes, like 'Hello' or "Hello".  
- For strings, + means "concatenate". 
- When a string is made of numeric characters, it is still a string. 
- We can convert a numeric string into a number using int().

### Reading & Converting

We prefer to read data in using strings, and then parse and convert the data as we need.  
This gives us more control over error situations and/or bad user input.  
Raw input numbers must be converted from strings.  
  
We can get at any single character in a string using an index specified in square brackets.  
The index value must be an integer and starts at zero.  
The index value can be an expression that is computed.  

- The built-in function **len()** returns the length of a string.
```py
fruit = 'banana'
print(len(fruit))
```

### Looping through strings

Using a while statement and an iterator, we can construct a loop to look at each character.
```py
fruit = 'banana'
index = 0
while index < len(fruit):
    character = fruit[index]
    print(index, character)
    index += 1
```

A definite loop using a for statement is much more elegant.  
The iterator (iteration variable) is completely taken care of by the for loop.  
```py
fruit = 'banana'
for i in fruit:
    print(i)
```

### Looping and counting

```py
word = 'amazing'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)
```

### Slicing strings

We can look at any section of a string using a **colon operator**.  
The second number is one beyond the end of the slice - "**up to but not including**".
```py
s = 'Monty Python'
print(s[0:4])  # Mont
print(s[6:8])  # Py
print(s[6:12]) # Python
```

**Note**: The above print statement reads "s sub zero through 4".  

If we leave off the first number or the last number of the slice, it is assumed to be  
the beginning or the end of the string respectively.
```py
s = 'Monty Python'
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:])  # Monty Python
```

### Using in as a logical operator

The **in** keyword can also be used to check if one string is **in** another string.  
In that case, **in** is a logical expression that returns a boolean.
```py
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)

for i in fruit:
    if i == 'a':
        print('Found it!')

if 'a' in fruit:
    print('This word contains the letter \'a\'.')
```

### String comparison

```py
word = input('Enter a word: ').lower()

if word == 'banana':
    print('All right, bananas!')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas!')
```






---
EOF