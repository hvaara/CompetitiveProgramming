def sieve(m):
    l = [True]*(int(m**.5)+2)
    l[0], l[1] = False, False
    for i in range(2, len(l)):
        if not l[i]:
            continue
        for j in range(i*2, len(l), i):
            l[j] = False
    return l

def solution(n):
    k = 100000000000
    c = 0
    for i, prime in enumerate(sieve(k)):
        if prime:
            c += 1
        if c == n:
            return i
    return -1

print(solution(10001))
