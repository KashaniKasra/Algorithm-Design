def DFS (adjacency, s, colors, component, N):
    component.append(s)
    colors[s] = "Black"

    for v in range (N):
        if ((adjacency[s][v] == 1) and (colors[v] == "White")):
            DFS(adjacency, v, colors, component, N)

def matching (connected, numbers, indexes):
    for component in connected:
        indx = []
        for num in component:
            indx.append(indexes[num])

        indx.sort()
        c = 0
        for i in indx:
            numbers[i] = component[c]
            c += 1

N = int(input())
numbers = list(map(int, input().split()))
adjacency = [[0 for i in range (N)] for i in range (N)]
colors = ["White" for i in range (N)]
connected = []
indexes = [0 for i in range (N)]
count = 0

for v in range (N):
    numbers[v] -= 1

for v in numbers:
    temp = input()
    i = 0
    for num in numbers:
        adjacency[v][num] = int(temp[i])
        i += 1

    indexes[v] = count
    count += 1

for s in range (N):
    if (colors[s] == "White"):
        component = []
        DFS(adjacency, s, colors, component, N)
        connected.append(component)

for c in connected:
    c.sort()

matching(connected, numbers, indexes)

for i in range (N):
    print(numbers[i] + 1, end = " ")