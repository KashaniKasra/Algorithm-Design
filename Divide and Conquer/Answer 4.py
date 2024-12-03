def divide(pi, start, end):
    if ((end - start) == 1):
        return (pi[start] + pi[end])
    
    mid = (start + end ) // 2
    left = pi[start : mid + 1]
    right = pi[mid + 1 : end + 1]
    maxL, maxR = 0, 0

    for i in range(len(left)):
        if (left[i] > maxL):
            maxL = left[i]
        if (right[i] > maxR):
            maxR = right[i]

    return max(divide(pi, start, mid) + maxR, divide(pi, mid + 1, end) + maxL ) 

n = int(input())
pi = list(map(int, input().split()))

result = divide(pi, 0, len(pi) - 1)

print(result)