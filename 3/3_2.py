# for loop
for i in range(0,41):
    if i == 13:
        continue
    elif i % 5 == 0 and i % 7 == 0:
        print(f'{i} is divided by 5 and 7')
    elif i % 5 == 0:
        print(f'{i} is divided by 5')
    elif i % 7 == 0:
        print(f'{i} is divided by 7')
    else:
        print(f'{i} is not important')

# while loop
x = 0
while x < 41:
    if x == 13:
        x += 1
        continue
    elif x % 5 == 0 and x % 7 == 0:
        print(f'{x} is divided by 5 and 7')
    elif x % 5 == 0:
        print(f'{x} is divided by 5')
    elif x % 7 == 0:
        print(f'{x} is divided by 7')
    else:
        print(f'{x} is not important')
    x += 1

    