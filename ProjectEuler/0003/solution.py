def sieve(m):
    l = [True]*(int(m**.5)+2)
    l[0], l[1] = False, False
    for i in range(2, len(l)):
        if not l[i]:
            continue
        for j in range(i*2, len(l), i):
            l[j] = False
    return l

def reverse_primes(l):
    for i in range(len(l)-1, 1, -1):
        if l[i]:
            yield i

def maxFactor(n):
    l = sieve(n)
    for prime in reverse_primes(l):
        if not n%prime:
            return prime

print(maxFactor(600851475143))
