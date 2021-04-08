a, b = map(int, input().split())
result = 0


def kimminsu(num: int):
    global result

    if num > b:
        return

    if a <= num <= b:
        result += 1

    kimminsu(num * 10 + 4)
    kimminsu(num * 10 + 7)


kimminsu(4)
kimminsu(7)
print(result)