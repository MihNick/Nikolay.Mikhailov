def IsPrime(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'
print(IsPrime(int(input())))
