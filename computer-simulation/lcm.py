# for lcm method you must need to find a good seed value.....

x0 = 37     # seed
a = 17      # constant multiplier
c = 31      # incrementor
m = 100     # modulus value

total = 10

print(x0, end=' ')
while total > 0:
    xi = (x0 * a + c) % m
    print(xi, end=' ')
    x0 = xi
    total -= 1

print()