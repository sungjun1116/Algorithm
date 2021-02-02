def cantor(x, l):
    m = (l - x) // 3
    if l - x == 1:
        return

    cantor(x, x + m)
    for i in range(x + m, x + 2 * m):
        data[i] = ' '
    cantor(x + 2 * m, x + 3 * m)
    return


while True:
    try:
        n = int(input())
        data = ["-" for i in range(3 ** n)]
        cantor(0, len(data))
        print(''.join(data))
    except:
        break