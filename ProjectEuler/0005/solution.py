def factors(n):
    f = {}
    for i in range(2, n+1):
        while not n%i:
            n //= i
            f[i] = f.get(i, 0) + 1
    return f

def findDivisors(n):
    f = {}
    for i in range(2, n+1):
        for (k,v) in factors(i).items():
            f[k] = max(f.get(k, 0), v)
    ret = 1
    for (k,v) in f.items():
        ret *= k**v
    return ret

print(findDivisors(20))
