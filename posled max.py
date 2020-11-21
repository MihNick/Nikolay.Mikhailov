a = [int(i) for i in input().split()]
print(max(a), len(a) - 1 - a[::-1].index(max(a)))
