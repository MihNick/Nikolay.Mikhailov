i = 0


def sum():
    global i
    n = int(input())
    if n != 0:
        i += n
        sum()
    elif n == 0:
        print(i)


sum()
