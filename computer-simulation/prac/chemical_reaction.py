delta_t = 0.1  # 0.1 sec
A0 = 100        # 100 gram
B0 = 50         # 50 gram

C0 = 0          # 0 gram

k1 = 0.008 
k2 = 0.002  

t = 0.0         # initial time
T = 5.0         # total or end time

print("\tTime\t\tA[i]\t\tB[i]\t\tC[i]")
print("%12.2f %15.2f %15.2f %15.2f"%(t, A0, B0, C0))

t += delta_t
while t < T:
    A = A0 + (k2 * C0 - k1 * A0 * B0) * delta_t           # decrease A
    B = B0 + (k2 * C0 - k1 * A0 * B0) * delta_t           # decrease B

    C = C0 + (2 * k1 * A0 * B0 - 2 * k2 * C0) * delta_t   # increase C
    A0, B0, C0 = A, B, C

    print("%12.2f %15.2f %15.2f %15.2f"%(t, A0, B0, C0))
    t += delta_t

