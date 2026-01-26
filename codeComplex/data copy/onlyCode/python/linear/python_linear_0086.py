import math

n = int(input())

# Assumption = they give it to me sorted by A

beacons = {}
sortedKeys = [0]*n

for i in range(n):
    a, b = map(int, input().split(' '))
    sortedKeys[i] = a
    beacons[a] = b

sortedKeys.sort()
maxA = sortedKeys[-1]

sumBeacons = [0]*(maxA+1)
count = 0
for a in range(maxA+1):
    sumBeacons[a] = count
    # Exclusive on the end value
    if a in beacons:
        count += 1

f = [0]*(n+1)
minF = math.inf
for i in range(1, n+1):
    a = sortedKeys[i-1]
    b = beacons[a]
    end = max(0, a-b)
    numDestroyed = sumBeacons[a] - sumBeacons[end]
    f[i] = numDestroyed
    if i-numDestroyed > 0:
        f[i] += f[(i-1)-numDestroyed]
    # Our answer is the minF of this value + all the ones before it we would have to destroy
    minF = min(minF, f[i]+n-i)

print(minF)