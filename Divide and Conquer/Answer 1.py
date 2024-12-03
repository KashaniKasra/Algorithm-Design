def divide (numbers, start, end, m, times, done):
    if (times[0] == m):
        done[0] = 1
        return
    if (start == end):
        return

    times[0] += 2

    mid = (start + end) // 2
    if (mid != 0):
        numbers[mid], numbers[mid - 1] = numbers[mid - 1], numbers[mid]
    else:
        numbers[mid + 1], numbers[mid] = numbers[mid], numbers[mid + 1]

    divide(numbers, start, mid - 1, m, times, done)
    if (done[0] == 1):
        return
    divide(numbers, mid, end, m, times, done)

n, m = map(int, input().split())
numbers = []
times = [1]
done = [0]

for i in range (n):
    numbers.append(i + 1)

if ((m % 2 == 0) or (m > 2 * n - 1)):
    print(-1)
else:
    divide(numbers, 0, n, m, times, done)

    for num in numbers:
        print(num, end = " ")