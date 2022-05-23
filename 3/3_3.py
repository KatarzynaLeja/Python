import math

file = open('vars.txt', 'x')

n = 2022
x = round(math.pi, 5)
word = "Python"
polish = "książka"

file.write(f'{n}\n{x}\n{word}\n{polish}')

file.close()

f = open('vars.txt', 'r')

for line in f:
    print(line)

f.close()