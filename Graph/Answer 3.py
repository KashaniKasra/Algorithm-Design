from heapq import heappush, heappop

def graph (adjacency, distances, d, edge, ans):
    if (edge == len(adjacency)):
        return

    if (distances[edge] == d):
        ans[0] += 1

    for adj in adjacency[edge]:
        adj_edge = adj[0]
        adj_dist = adj[1]

        if (edge >= adj_edge):
            continue

        if (distances[edge] >= d):
            if (distances[adj_edge] < d < distances[adj_edge] + adj_dist):
                ans[0] += 1

        elif (distances[adj_edge] >= d):
            if (distances[edge] < d < distances[edge] + adj_dist):
                ans[0] += 1

        else:
            sum_rem = (d - distances[edge]) + (d - distances[adj_edge])

            if (sum_rem == adj_dist):
                ans[0] += 1
            elif (sum_rem < adj_dist):
                ans[0] += 2

    graph(adjacency, distances, d, edge + 1, ans)

def dijkstra (adjacency, distances, s):
    queue = []
    max_distance = 10 ** 15
    heappush(queue, [0, s])

    for i in range (len(adjacency)):
        distances.append(max_distance)

    distances[s] = 0

    while (len(queue) > 0):
        distance, pare = heappop(queue)

        for adj in adjacency[pare]:
            adj_edge = adj[0]
            adj_dist = adj[1]

            if (distances[adj_edge] > distances[pare] + adj_dist):
                distances[adj_edge] = distances[pare] + adj_dist
                heappush(queue, (distances[adj_edge], adj_edge))

n, m, s = map(int, input().split())
adjacency = []
distances = []
ans = [0]

for i in range (n):
    adjacency.append([])

for i in range (m):
    u, v, w = map(int, input().split())

    adjacency[u - 1].append([v - 1, w])
    adjacency[v - 1].append([u - 1, w])

d = int(input())

dijkstra(adjacency, distances, s - 1)

graph(adjacency, distances, d, 0, ans)

print(ans[0])