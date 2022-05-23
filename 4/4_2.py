L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# iterative version
def reverse_range(L, left, right):
    l1 = []
    for n in L[left: right+1]:
        l1.insert(0, n)
    L[left:right+1] = l1
    return L

print(reverse_range(L, 3, 6))

# recursive version
def rev_range(L, left, right):
    if len(L) == 0:
        return L
    else:
        return [L.pop()] + rev_range(L, left, right)

print(rev_range(L, 3, 6))