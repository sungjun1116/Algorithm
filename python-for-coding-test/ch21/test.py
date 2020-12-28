n = int(input())
word = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]

# 나오는 횟수를 alpha 테이블에 기록하는데 자릿수마다 weight를 다르게 줌
alphabet = [0] * 26

for i in range(n):
    word[i].sort(reverse=T)
    j = 0
    for w in word[i]:
        alphabet[w] += (10**j)
        j += 1
