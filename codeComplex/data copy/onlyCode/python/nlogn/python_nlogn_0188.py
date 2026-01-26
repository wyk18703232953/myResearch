n = int(input())
a = list(map(int, input().split()))
ans = 0
sum = 0
mp = {}
for i in range(n):
    x = a[i]
    ans += (x * i) - sum;
    ans -= (mp.get(x - 1, 0));
    ans -= (-mp.get(x + 1, 0));
    mp[x] = mp.get(x, 0) + 1;
    sum += x;
print(ans)