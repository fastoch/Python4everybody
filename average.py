counter = 0
total = 0
print('Counter:', counter, 'Total:', total)
for i in [4, 16, -29, 32]:
    counter+=1
    total+=i
    print('Counter:', counter, 'added value:', i, 'Total:', total)
average = total/counter
print('Counter:', counter, 'Total:', total, 'Average:', average)