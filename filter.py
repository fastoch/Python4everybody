counter = 0
total = 0
for value in [7, 36, 42, 1, 16, 33, 64]:
    if value > 30:
        print('Greater than 30',value)
        counter+=1
    total +=1
print(counter, 'values', 'out of', total, 'are greater than 30')