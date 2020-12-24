import itertools


vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())

array = list(input().split())
array.sort()

# 길이가 l인 모든 암호 조합을 확인
for x in itertools.combinations(array, l):
    count = 0
    for i in x:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if 1 <= count <= l - 2:
        print(''.join(x))