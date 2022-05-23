import itertools
import random
# Create the following infinite iterators:
# (a) returning 0, 1, 0, 1, 0, 1, ...,

iter1 = itertools.cycle([0, 1])

k = 0
for i in iter1:
    k += 1
    print(i)
    if k > 5:
        break

# (b) returning random sequence with 0 and 1

def i01():
    while True:
        yield random.randint(0, 1)

iter2 = i01()
k = 0
for i in iter2:
    k +=1
    print(i)
    if k > 10:
        break

# (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...

iter3 = itertools.cycle([0, 1, 0, -1])
x = 0
for i in iter3:
    x +=1 
    print(i)
    if x > 5:
        break

