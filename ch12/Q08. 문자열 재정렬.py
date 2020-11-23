array = input()
letters = []
digits = 0

for data in array:
    if data.isdigit():  # isalpha(), isalnum()도 존재함!
        digits += int(data)
    else:
        letters.append(data)

letters.sort()

if digits != 0:  # 예외처리를 생각 못함!
    letters.append(str(digits))

print(''.join(letters))









