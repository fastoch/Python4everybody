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
In Python, comments are marked with a pawn sign #.

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
- You can also use int() and float() to convert strings, but you'll get an error if the string
does not contain numeric characters.

---

## Chapter 5 - Loops & iteration

Loops have iteration variables that change each time through a loop.
```py
n = 10
while (n > 0):
    print(n)
    n = n-1
print('Blastoff!')
print(n)
```





---
EOF