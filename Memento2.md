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

## What is not a "Collection"

Most of our variables have one value in them, and when we put a new value in the variable, the old one is overwritten.  
A **collection** allows us to put **many values** in **a single variable**.  

A list is a kind of collection.  
`friends = ['Monica', 'Rachel', 'Chandler', 'Ross']`



---
EOF