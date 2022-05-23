roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

# metoda 1
D = {}

for x in range(len(roman)):
    D[roman[x]] = arabic[x]


# metoda 2

D2 = {roman[i]: arabic[i] for i in range(len(roman))}


# metoda 3

D3 = dict((roman[i], arabic[i]) for i in range(len(roman)))
