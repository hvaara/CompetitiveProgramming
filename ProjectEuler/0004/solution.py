def numberGen(n):
    for i in range(10**n, 10**(n-1), -1):
        for j in range(10**n, 10**(n-1), -1):
            yield i*j

def largestPalindrome(n):
    return max(x for x in numberGen(n) if str(x) == str(x)[::-1])

print(largestPalindrome(3))
