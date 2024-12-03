def dynamic (dp, n, m, numbers, powers):
    for unit in range (n + 1):
        temp = []
        picked = []
        remains = []
        for indx in range (m):
            remain = unit - powers[numbers[indx]]
            if (remain >= 0):
                temp.append(dp[remain])
                picked.append(numbers[indx])
                remains.append(remain)

        chosen = -1
        maxLength = -1
        for num in range (len(temp)):
            tempLength = 0
            for digit in range (m):
                tempLength += temp[num][digit]
            if ((tempLength == 0) and (remains[num] != 0)):
                continue
            if (tempLength > maxLength):
                maxLength = tempLength
                chosen = num
            elif (tempLength == maxLength):
                for digits in range (m):
                    if (temp[num][digits] > temp[chosen][digits]):
                        maxLength = tempLength
                        chosen = num
                        break
                    elif (temp[num][digits] < temp[chosen][digits]):
                        break

        if (chosen != -1):
            for index in range (m):
                if (numbers[index] != picked[chosen]):
                    dp[unit][index] = temp[chosen][index]
                else:
                    dp[unit][index] = temp[chosen][index] + 1

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [[0 for i in range (m)] for i in range (n + 1)]
powers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
result = ""

numbers.sort(reverse = True)

dynamic (dp, n, m, numbers, powers)

for indx in range (m):
    result += (dp[n][indx]) * str(numbers[indx])

print(result)