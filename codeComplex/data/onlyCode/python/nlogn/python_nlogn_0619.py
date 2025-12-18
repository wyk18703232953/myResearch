n = input()
ans = 0
j = 2
for i in range(2,n/2 + 1):
    while i * j <= n:
        ans += j * 4
        #print(ans)
        j += 1
    else :j = 2
print(ans)