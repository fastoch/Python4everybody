max = 0
for i in [9,74,51,-12,-82,0]:
    if i < 0:
        continue
    elif i > max:
        max = i
if max == 0:
    print("All numbers in this list are negative or equal to zero")
else:
    print("The largest number in the list is: ",max)
