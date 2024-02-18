var = input("Enter a number: ")
try:
    int(var) # fails if the input is not a number
    print("The number you entered is "+var) # executed only if you enter a number
except:
    print("Not a number!") # executed if you don't enter a number