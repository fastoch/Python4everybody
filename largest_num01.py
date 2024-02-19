largest = -1
for num in [-9,-41,-12,-3,-74,-15]:
    if num > largest:
        largest = num
if largest == -1:
    print('I didn\'t find any number larger than -1')
else:
    print('The largest number is', num)