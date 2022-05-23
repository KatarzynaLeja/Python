line = '+---'

word = input('Choose your word: ')

for i in range(len(word)):
    print(line, end='')
print('+')

for i in word:
    print(f'| {i} ', end='')
print('|')

for i in range(len(word)):
    print(line, end='')
print('+')