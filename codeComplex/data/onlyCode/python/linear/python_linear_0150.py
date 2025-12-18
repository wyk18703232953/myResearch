n, p = map(int, input().split())

arr = [int(b) for b in input().split()]

res = []

prefsums = [arr[0]]

for i in range(1, n):
    prefsums.append(prefsums[i - 1] + arr[i])

allsum = sum(arr)

if len(arr) == 2:
    print(arr[0] % p + arr[1] % p)
    exit()

for i in range(1, n - 1):
    res.append((prefsums[i] % p) + ((allsum - prefsums[i]) % p))


print(max(res))

