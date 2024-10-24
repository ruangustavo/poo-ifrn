a, b = 0, 1
print(a)
print(b)
for _ in range(8):
    a, b = b, a + b
    print(b)
