# doesn't work if all the numbers in my list are negative 
max = 0
for i in [-20,-80,-10,-65,-32]:
    if i > max:
        max = i
    
print("The largest number in the list is: ",max)
