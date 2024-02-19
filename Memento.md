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

#### What is the largest number?
```py
largest = -1
for num in [9,41,12,3,74,15]:
    if num > largest:
        largest = num
if largest == -1:
    print('I didn\'t find any number larger than -1')
else:
    print('The largest number is', num)
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

### Search using a boolean variable
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

---

## Chapter 6 - 





---
EOF