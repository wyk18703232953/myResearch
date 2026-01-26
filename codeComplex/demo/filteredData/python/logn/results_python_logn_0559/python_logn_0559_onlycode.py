sum = [0 for i in range(12)]
i = 0
while sum[i] < 10 ** 12:
    i += 1
    sum[i] = sum[i - 1] + i * (10 ** i - 10 ** (i - 1))
k = int(input())
i = 0
while k > sum[i]:
    i += 1
ans = 10 ** (i - 1) - 1
ans += (k - sum[i - 1]) // i
if (k - sum[i - 1]) % i != 0:
    ans += 1
print(str(ans)[(k - sum[i - 1]) % i - 1])