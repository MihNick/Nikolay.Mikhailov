a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j, c = 0, 0, []
for _ in range(len(a) + len(b)):
    if (j == len(b)) or (i < len(a) and a[i] < b[j]):
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print(*c)
