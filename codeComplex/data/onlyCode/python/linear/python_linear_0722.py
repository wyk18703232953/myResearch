import sys


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None


n, m = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))
firstMax = max(boys)
secondMax = second_largest(boys)
minGrills = min(girls)
minSum = 0
if firstMax > minGrills:
    print(-1)
    sys.exit()
elif firstMax == minGrills:
    minSum = m * (sum(boys) - firstMax) + sum(girls)
elif n == 1:
    print(-1)
    sys.exit()
else:
    minSum = m * sum(boys) + sum(girls) - (m-1) * firstMax - secondMax
print(minSum)
