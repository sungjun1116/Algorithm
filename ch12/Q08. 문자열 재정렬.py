array = input()
letters = []
digits = 0

for data in array:
    if data.isdigit():
        digits += int(data)
    else:
        letters.append(data)

letters.sort()

# 예외처리를 생각 못함!
if digits != 0:
    letters.append(str(digits))

print(''.join(letters))









