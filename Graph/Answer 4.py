def kruskal (weightedEdges, disjoint, N, newEdge, ans):
    count = N + 1

    for edge in weightedEdges:
        if (disjoint[edge[0]] != disjoint[edge[1]]):
            if (edge == newEdge):
                ans.append("Yes")
                return
            
            temp0 = disjoint[edge[0]]
            temp1 = disjoint[edge[1]]
            for i in range(1, len(disjoint)):
                if ((disjoint[i] == temp0) or (disjoint[i] == temp1)):
                    disjoint[i] = count
            count += 1

    ans.append("No")
    return

N, M, Q = map(int, input().split())
weightedEdges = []
ans = []

for i in range (M):
    u, v, w = map(int, input().split())

    if (u != v):
        weightedEdges.append([u, v, w])

weightedEdges = sorted(weightedEdges, key = lambda l:l[2])

for q in range (Q):
    u, v, w = map(int, input().split())

    if (u == v):
        ans.append("No")
    else:
        disjoint = []
        for i in range (N + 1):
            disjoint.append(i)

        for i in range (len(weightedEdges)):
            if (w < weightedEdges[i][2]):
                weightedEdges.insert(i, [u, v, w])
                index = i
                break
            if (i == len(weightedEdges) - 1):
                weightedEdges.append([u, v, w])
                index = i

        kruskal(weightedEdges, disjoint, N, [u, v, w], ans)

        weightedEdges.pop(index)

for result in ans:
    print(result)