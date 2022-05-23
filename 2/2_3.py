# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].

numbers = []

for i in range (1, 2022, 2):
    n = i * i
    numbers.append(n)

suma = sum(numbers)
print(suma)