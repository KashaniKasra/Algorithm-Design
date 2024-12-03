def divide (W, k, start, end, result, round):
    if (start == end):
        if (abs(W[start]) > k):
            result[round] += 1
        return
    
    mid = (start + end) // 2

    divide(W, k, start, mid, result, round)
    divide(W, k, mid + 1, end, result, round)
    merge(W, k, start, mid, end, result, round)

def merge (W, k, start, mid, end, result, round):
    left = W[start : mid + 1]
    right = W[mid + 1 : end + 1]
    sumL = [left[-1] for i in range (len(left))]
    sumR = [right[0] for i in range (len(right))]
    _sumL = []
    k_r, _k_r = [], []
    l, r, _l, _r = 0, 0, 0, 0

    for i in range (len(left) - 2, -1, -1):
        sumL[i] = sumL[i + 1] + left[i]
    for i in range (1, len(right)):
        sumR[i] = sumR[i - 1] + right[i]

    for num in sumR:
        k_r.append(k - num)
        _k_r.append(-k - num)
    for num in sumL:
        _sumL.append(num)

    sumL.sort()
    k_r.sort()
    _sumL.sort(reverse = True)
    _k_r.sort(reverse = True)

    while (l < len(sumL) and r < len(k_r)):
        if (sumL[l] > k_r[r]):
            r += 1
            result[round] += len(sumL) - l
        else:
            l += 1
    while (_l < len(_sumL) and _r < len(_k_r)):
        if (_sumL[_l] < _k_r[_r]):
            _r += 1
            result[round] += len(_sumL) - _l
        else:
            _l += 1

T = int(input())
result = []

for round in range (T):
    n, k = map(int, input().split())
    W = list(map(int, input().split()))
    result.append(0)

    divide(W, k, 0, n - 1, result, round)

for ans in result:
    print(ans)