exp = list(input().split('-'))

result = []
for minus in exp:
    temp = list(map(int, minus.split('+')))
    result.append(sum(temp))

print(result[0] - sum(result[1:]))