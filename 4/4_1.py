# (a) a test if p is in unit circle

circle = lambda x, y: 'p is in unit circle' if x*x + y*y == 1 else 'p is not in unit circle'
print(circle(0, 0))

# (b) a test if the coordinates of p are positive

cor = lambda x, y: 'Coordinates are positive.' if x > 0 and y > 0 else 'Coordinates are not positive.'
print(cor(2, 0))

# (c) a sorting key (y decreasing, x increasing)

p1 = [(2, 0), (-3, 5), (2, 4), (0, -2), (7, 4), (1, 4)]

p1.sort(key=lambda p: (-p[1], p[0]))
print(p1)

# (d) a sorting key (the sum |x|+|y|).

p2 = [(2, 0), (-2, 5), (0, -3), (4, 5), (3, 3), (-1, -5)]
p2.sort(key=lambda p: p[0] + p[1])
print(p2)

