fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)

for i in fruit:
    if i == 'a':
        print('Found it!')

if 'a' in fruit:
    print('This word contains the letter \'a\'.')