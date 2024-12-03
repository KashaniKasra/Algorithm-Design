def graph (houses, blacks, N, M):
    last = []
    for i in range (len(blacks)):
        last.append([blacks[i][0], blacks[i][1]])
    
    while (len(blacks) != 0):
        tempBlacks = []
        temp = []
        temp.append(last)
        last = []

        for i in range (len(blacks)):
            n = blacks[i][0]
            m = blacks[i][1]

            if (n + 1 < N):
                if (houses[n + 1][m] == "White"):
                    tempBlacks.append([n + 1, m])
                    last.append([n + 1, m])
                    houses[n + 1][m] = "Black"
            if (n - 1 >= 0):
                if (houses[n - 1][m] == "White"):
                    tempBlacks.append([n - 1, m])
                    last.append([n - 1, m])
                    houses[n - 1][m] = "Black"
            if (m + 1 < M):
                if (houses[n][m + 1] == "White"):
                    tempBlacks.append([n, m + 1])
                    last.append([n, m + 1])
                    houses[n][m + 1] = "Black"
            if (m - 1 >= 0):
                if (houses[n][m - 1] == "White"):
                    tempBlacks.append([n, m - 1])
                    last.append([n, m - 1])
                    houses[n][m - 1] = "Black"

        blacks = []
        for j in range (len(tempBlacks)):
            blacks.append([tempBlacks[j][0], tempBlacks[j][1]])

    if (len(temp) > 0):
        last = temp[0]

    last = sorted(last, key = lambda l:l[0])
    temp = [last[0][0], last[0][1]]
    for l in last:
        if (l[0] != temp[0]):
            break
        if (l[1] < temp[1]):
            temp = [l[0], l[1]]
    ans = temp

    return ans

N, M = map(int, input().split())
K = int(input())
temp = list(map(int, input().split()))
houses = [["White" for i in range (M)] for i in range (N)]
blacks = []

for i in range (0, len(temp), 2):
    houses[temp[i] - 1][temp[i + 1] - 1] = "Black"
    blacks.append([temp[i] - 1, temp[i + 1] - 1])

ans = graph(houses, blacks, N, M)

print(ans[0] + 1, ans[1] + 1)