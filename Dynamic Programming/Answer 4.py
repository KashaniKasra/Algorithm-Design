def dynamic (dp, numbers, n, x, maxSum):
    dp[1][numbers[0]][1] = 1

    for num in range (n + 1):
        dp[num][0][0] = 1
    
    for num in range (2, n + 1):
        for sum in range (0, maxSum + 1):
            for amount in range (n + 1):
                dp[num][sum][amount] = dp[num - 1][sum][amount]
            remain = sum - numbers[num - 1]
            if (remain >= 0):
                for amount in range (n):
                    dp[num][sum][amount + 1] += dp[num - 1][remain][amount]
                  
n, x = map(int, input().split())
numbers = list(map(int, input().split()))
newNumbers = []
maxSum = 0
result = 0

for number in numbers:
    if (number <= (x * n)):
        newNumbers.append(number)
        maxSum += number
        
n = len(newNumbers)
dp = [[[0 for i in range (n + 1)] for i in range (maxSum + 1)] for i in range (n + 1)]

if (n == 0):
    pass
elif (n == 1):
    if (newNumbers[0] == x):
        result = 1
else:
    dynamic(dp, newNumbers, n, x, maxSum)

    for sum in range (1, maxSum + 1):
        for amount in range (1, n + 1):
            times = dp[n][sum][amount]
            if ((amount > 0) and (times > 0)):
                if ((sum / amount) == x):
                    result += times

print(result)