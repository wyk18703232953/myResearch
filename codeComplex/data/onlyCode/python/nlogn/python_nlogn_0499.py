# RawCoder : https://bit.ly/RCyouTube
# Author : MehulYK

n, m = map(int, input().split())
sun, su, ans = 0, 0, 0
arr, brr, dif = [], [], []
for i in range(n):
    a, b = map(int, input().split())
    #arr.append(a)
    #brr.append(b)
    sun += a; su += b
    dif.append(a - b)
if(su > m):print(-1)
elif(sun == m):print(0)
else:
    dif.sort()
    j = n - 1
    while(sun > m):
        sun -= dif[j]
        ans += 1
        j -= 1
    print(ans)    