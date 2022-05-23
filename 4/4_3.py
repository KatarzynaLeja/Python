def iter_even():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1

for x in iter_even():
    print(x)
    if x > 100:
        break

def iter_odd():
    i = 0
    while True:
        if i % 2 != 0:
            yield i
        i += 1

for n in iter_odd():
    print(n)
    if n > 100:
        break


def iter_power(k):
    i = 0
    while True:
        yield k ** i
        i += 1

for n in iter_power(3):
    print(n)
    if n > 900:
        break