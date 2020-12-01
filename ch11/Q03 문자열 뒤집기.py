data = list(map(int, input()))
cnt = 0
for i in range(1, len(data)):
    #  첫 번째 원소와 다르거나 바뀔때
    if data[0] != data[i] and data[i] != data[i - 1]:
        cnt += 1

print(cnt)


''' 구글링

S = input()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count + 1) // 2)

0 과 1 👉 0번, 길이 1

01 👉 1번, 길이 2

010 👉 1번, 길이 3

0101 👉 2번, 길이 4

01010 👉 2번, 길이 5

010101 👉 3번, 길이 6

0101010 👉3번, 길이 7
'''