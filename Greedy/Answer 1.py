def greedy (n, m, k):
    used = n
    targetR = 0
    targetL = 0
    ans = 1

    while (used < m):
        ans += 1
        used += targetR + targetL + 1

        if (targetR + 1 < n - k):
            targetR += 1
        if (targetL + 1 <= k):
            targetL += 1

        if (used == m):
            break
        elif (used > m):
            ans -= 1
            break

    return ans


n, m, k = map(int, input().split())

ans = greedy(n, m, k - 1)

print(ans)