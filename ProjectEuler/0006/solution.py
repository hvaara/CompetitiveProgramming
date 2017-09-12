def solution(n):
    return sum(x for x in range(1, n+1))**2 - sum(x**2 for x in range(1, n+1))

print(solution(100))
