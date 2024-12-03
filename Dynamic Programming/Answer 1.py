def dynamic (dp, moves, minMove, k):
    for choc in range (minMove, k + 1):
        ans1 = 2
        ans2 = 1
        for move in  moves:
            if (move <= choc):
                ans1 = dp[2][choc - move]
                if (ans1 == 1):
                    break
        for move in moves:
            if (move <= choc):
                ans2 = dp[1][choc - move]
                if (ans2 == 2):
                    break
        dp[1][choc] = ans1
        dp[2][choc] = ans2

n, k = map(int, input().split())
moves = list(map(int, input().split()))
dp = [[0 for i in range (k + 1)] for i in range (3)]

minMove = min(moves)

if (minMove < k):
    for i in range (minMove):
        dp[1][i] = 2
        dp[2][i] = 1

    dynamic(dp, moves, minMove, k)

    if (dp[1][k] == 1):
        print("First")
    elif (dp[1][k] == 2):
        print("Second")
elif (minMove > k):
    print("Second")
else:
    print("First")