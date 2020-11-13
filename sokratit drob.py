def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)
n = int(input())
m = int(input())


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)
print(*ReduceFraction(n, m))
