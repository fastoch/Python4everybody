max = None
for i in [-20,-80,-10,-65,-32]:
    if max == None:
        max = i
    elif i > max:
        max = i
print("The largest number in the list is: ",max)
