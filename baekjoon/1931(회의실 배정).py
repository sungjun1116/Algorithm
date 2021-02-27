n = int(input())

meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 1
value = meetings[0][1]
for i in range(1, len(meetings)):
    if value <= meetings[i][0]:
        count += 1
        value = meetings[i][1]

print(count)