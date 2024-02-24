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



---
EOF