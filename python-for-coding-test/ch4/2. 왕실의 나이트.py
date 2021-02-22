input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
    now_row = row + step[0]
    now_column = column + step[1]

    if 1 <= now_row <= 8 and 1 <= now_column <= 8:
        result += 1

print(result)