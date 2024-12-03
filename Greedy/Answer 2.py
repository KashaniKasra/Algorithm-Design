def greedy (energies, n, result, test):
    if (n == 0):
        return
    if (energies[0] != 1):
        result[test] += n
        return
    if (n == 1):
        result[test] += 1
        return
    
    result[test] += 1
    energies[1] -= 1
    if (energies[1] == 0):
        energies.pop(1)
    energies.pop(0)

    greedy(energies, len(energies), result, test)

t = int(input())
result = []

for test in range (t):
    n = int(input())
    energies = list(map(int, input().split()))

    result.append(0)
    energies.sort()

    greedy(energies, n, result, test)

for ans in result:
    print(ans)