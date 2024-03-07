Timeline: from 205 to 410 min

# Chapter 7 - Reading Files

## File processing

A text file can be thought as a sequence of lines.  
Before we can read the contents of the file, we must tell Python which  
file we are going to work with, and what we'll be doing with the file.  
  
This is done with the **open()** function.  
open() returns a "**file handle**" - a variable used to perform operations  
on the file. Similar to "File -> Open" in a Word Processor.  
  
syntax is: `handle = open(filename, mode)`  
example: `fhand = open('mbox.txt', 'r')`  

The filename (or file path) is a string.  

The mode is optional and should be:
- 'r' if we want to read the file 
- 'w' if we want to write the file
  
We use a special character called the **newline** to indicate when a line ends.  
We represent it as **\n** in strings. Newline is still one character, not two.
`len('A\nB')` returns 3  
  
A text file has newlines at the end of each line.  

## Reading files in Python

### File Handle as a Sequence

A file handle open for read can be treated as a sequence of strings where each line  
in the file is a string in the sequence. We can use the **for** statement to iterate  
through a sequence. Remember - a sequence is an **ordered set**.

```py
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese) # for each line in the file handle, print out the current line 
```

Other languages like C or C++ require to write while loops with end of file (EOF)  
conditions and all kinds of things that make this very difficult.
  
### Counting lines in a file

- open a file read-only
- use a for loop to read each line
- count the lines and print out the result

```py
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line count:', count)
```

### Reading the *whole* file

We can read the whole file (newlines and all) into a single string.
```py
fhand = open('mbox.txt')
inp = fhand.read() # store the file as one big string
print(len(inp))
print(inp[:20]) # print the first 20 characters, from index 0 to 19
```

### Searching through a file

We can put an if statement in a for loop to only print lines that meet some criteria.
```py
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
```
This little program will print lines that start with 'From:', but they also return blank lines.  
**Explanation**: each line from the file has a newline at the end. The print statement adds another newline to each line.  
  
**Fix**: we can strip the whitespace from the right-hand side of the line using **rstrip()** from the string library.  
The newline is considered whitespace and is stripped.
```py
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line.rstrip())
```

### Using **in** to select lines 

We can look for a string anywhere in a line as our selection criteria.
```py
fhand = open('mbox.txt')
for line in fhand:
    if '@uct.ac.za' in line:
        print(line.rstrip())
```

### Prompt for file name

```py
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count+=1
print('There were', count, 'subject lines in', fname)
```

### Bad user input

```py
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File \"' + fname + '\" cannot be found.')
    quit() # if you cannot open the file, quit the program
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count+=1
print('There were', count, 'subject lines in', fname)
```

---

# Chapter 8 - Lists

## Programming

- **Algorithms**: a set of rules or steps used to solve a problem.  
- **Data Structures**: a particular way of organizing data in a computer.  
  
Lists are the first and simplest data structure.

## What is a "Collection"

Most of our variables have one value in them, and when we put a new value in the variable, the old one is overwritten.  
A **collection** allows us to put **many values** in **a single variable**.  

A list is a kind of collection: 
`friends = ['Monica', 'Rachel', 'Chandler', 'Ross']`

List constants are surrounded by square brackets and the elements in the list are separated by commas.
- A list element can be any Python object, even another list.  
- A list can be empty.  
- A list can contain different types of data.  
  
Just like strings, we can get any single element in a list using an index specified in square brackets.
`print friends[1]`

Strings are **immutable**, we cannot change the contents of a string. We must make a new string.  
Lists are **mutable**, we can change an element of a list using the index operator.
`friends[1] = 'Phoebe'`

The **len()** function takes a list as a parameter and returns the number of elements in the list.  
Actually, **len()** tells us the number of elements of any set or sequence.

## Using the range() function

The range() function returns a list of numbers that range from zero to one less than the parameter.
We can construct an index loop using **for** and an integer **iterator**.

2 for loops that achieve the same result:
```py
friends = ['Monica', 'Rachel', 'Chandler', 'Ross']
for friend in friends:
    print('Hello', friend)
for i in range(len(friends)):
    friend = friends[i]
    print('Hello', friend)
```

## Loop operations

### Concatening lists using +

We can create a new list by adding 2 existing lists together:
```py
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
```

### Slicing lists using the colon operator ":"

```py
t = [9,41,12,3,74,15]
print(t[1:3]) # [41,12]
print(t[:4])
print(t[3:])
```
**Remember**: just like in strings, the second number is "up to but not including". 

## List Methods

```py
x = list()
print(type(x)) # <class 'list'>
print(dir(x)) # lists all methods available for an object of class 'List'
```

### Building a list from scratch

We can create an empty list and then add elements using the **append()** method.  
The list stays in order and new elements are added at the end of the list.
```py
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
```

### Is something in a list?

Python provides 2 operators that let you check if an item is in a list.  
These are logical operators that return True or False.  
They do not modify the list.

```py
some = [1,9,21,10,16]
print(9 in some)
print(15 in some)
print(20 not in some)
```

### Sorting lists

```py
friends = ['Sally', 'Billy', 'Harry']
friends.sort()
print(friends) # ['Billy', 'Harry', 'Sally']
```

**Remember**: strings are not mutable, but lists are mutable.  
String methods like upper() or lower() create a new string, while sort() does not create a new list.

### Built-in functions & Lists

There are a number of functions built into Python that take lists as parameters.  
```py
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
```

## Strings vs. Lists

**Split()** breaks a string into parts and produces a list of strings.  
We think of these as words. We can access a particular word or loop through all the words.
```py
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
```

When you do not specify a **delimiter**, split() looks for white spaces (tabs, newlines, spaces).  
Multiple spaces are treated like a single one.
You can specify what delimiter character to use in the **splitting**.  
```py
line = 'A lot         of spaces'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))
```

**Filter emails** received in **January** and print the sender (2nd word in the line):
```py
fhand = open('mbox.txt')
for line in fhand:
    if not line.startswith('From') : continue # ignore lines not starting with 'From'
    if 'Jan' in line:
        words = line.split()
        print(words[1])
```


test



---
EOF