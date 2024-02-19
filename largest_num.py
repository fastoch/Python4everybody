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
