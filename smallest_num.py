min = None
for i in [20,80,10,65,32]:
    if min == None:
        min = i
    elif i < min:
        min = i
print("The largest number in the list is: ",min)
