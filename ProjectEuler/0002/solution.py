def genFib(m=float('inf')):
    a, b = 1, 1
    while a < m:
        a, b = b, a+b
        yield a

print(sum(x for x in genFib(4000000) if not x%2))
