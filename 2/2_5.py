S = '''April is the cruellest month, breeding
Lilacs out of the dead land, mixing
Memory and desire, stirring
Dull roots with spring rain.
Winter kept us warm, covering
Earth in forgetful snow, feeding
A little life with dried tubers.'''

# Find the number of black characters in S

black = 0

for i in S:
    if i.isspace() == False:
        black += 1

print(f'The number of black character in S: {black}')

# Find the number of words in S

words = S.split()
print(f'The number of words in S: {len(words)}')

# Find the longest word in S

lenght = 0
for x in words:
    if len(x) > lenght:
        lenght = len(x)
        longest = x
        
print(f'The longest word in S is {longest}')

# Sort words from S according to (1) the lexicographic order, (2) the length
# 1

lexi = words
lexi.sort(key=str.lower)


# 2
leng = words
leng.sort(key=len)

