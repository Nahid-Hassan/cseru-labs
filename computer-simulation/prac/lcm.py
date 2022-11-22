x0, a, c, m = 37, 27, 31, 100

print(x0, end=' ')
total = 10
total -= 1

while total > 0:
    total -= 1
    x1 = (x0 * a + c) % m
    print(x1, end = ' ')
    x0 = x1

print()