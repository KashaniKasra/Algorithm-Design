def mergeSort (A, start, end, result):
    if (start >= end):
        return
    
    mid = (start + end) // 2

    mergeSort(A, start, mid, result)
    mergeSort(A, mid + 1, end, result)
    merge(A, start, mid, end, result)

def merge (A, start, mid, end, result):
    left = A[start : mid + 1]
    right = A[mid + 1 : end + 1]
    l = 0
    r = 0
    a = start

    while (l < len(left) and r < len(right)):
        if (left[l] > right[r]):
            A[a] = right[r]
            r += 1
            result[0] += mid - l - start + 1
        else:
            A[a] = left[l]
            l += 1
        a += 1

        if (l >= len(left)):
            A[a : end + 1] = right[r : end + 1]
            break
        if (r >= len(right)):
            A[a : end + 1] = left[l : mid + 1]
            break

n = int(input())
arr = list(map(int, input().split()))
result = [0]

mergeSort(arr, 0, n - 1, result)

print(result[0])