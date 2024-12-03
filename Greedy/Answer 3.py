def greedy (limits, start, end):
    if (start == end):
        return "sad"

    total = 0
    for i in limits:
        total += i
    total -= len(limits)

    ones = 0
    for j in limits:
        if (j == 1):
            ones += 1
    
    if (total < ones):
        return "sad"

    return "happy"

t = int(input())
result = []

for test in range (t):
    n, q = map(int, input().split())
    limits = list(map(int, input().split()))

    for customer in range (q):
        start, end = map(int, input().split())

        ans = greedy(limits[start - 1 : end], start - 1, end - 1)

        result.append(ans)

for i in result:
    print(i)