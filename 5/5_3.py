import random

def random_walk(start):

    while True:
        start = start + random.choice([-1, 1])
        yield start
        

gen = random_walk(0)

for i in range(100):
    if i < 99:
        next(gen)
    else:
        print(f'The final position after 100 moves is: {next(gen)}')


