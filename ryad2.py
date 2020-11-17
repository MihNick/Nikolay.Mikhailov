a = int(input())
b = int(input())
c = 1
if b > a:
    b = b + 1
else:
    b = b - 1
    c = -1
for i in range(a, b, c):
    print(i, end=' ')
