def dynamic (dp, cost):
    length = 1
    for end in range(n - 1, -1, -1):
        for i in range (0, end):
            j = i + length
            costTemp = 0
            for x in range (i, j + 1):
                costTemp += cost[x]
            min = float('inf')
            for k in range (i, j):
                temp = dp[i][k] + dp[k + 1][j] + costTemp
                if (temp < min):
                    min = temp
            dp[i][j] = min
        length += 1

n = int(input())
numbers = list(map(int, input().split()))
dp = [[0 for i in range (n)] for i in range (n)]

dynamic(dp, numbers)

print(dp[0][n - 1])