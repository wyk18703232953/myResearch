# coding: utf-8
# Your code here!
import sys
n = int(input())

a = list(map(int,input().split()))

for i in range(n):
    a[i] = [i,a[i]]

a.sort(key=lambda x: x[1],reverse=True)

ans = []

index = 0
cnt = 0
tmp = 1
right_bool = False
left_bool = False

for i in range(1,n):
    if a[index][1] == 0:
        print('NO')
        sys.exit()
    if a[i][1] >= 2:
        ans.append([a[i-1][0],a[i][0]])
        cnt += 1
        a[i-1][1] -= 1
        a[i][1] -= 1
    else:
        if right_bool == False:
            ans.append([a[i-1][0],a[i][0]])
            a[i-1][1] -= 1
            a[i][1] -= 1
            cnt += 1
            right_bool = True
        else:
            ans.append([a[index][0],a[i][0]])
            a[index][1] -= 1
            a[i][1] -= 1
            if left_bool == False:
                cnt += 1
                left_bool = True
            if a[index][1] == 0:
                index += 1
        
print('YES', cnt)
print(n-1)
for i in range(n-1):
    print(ans[i][0]+1,ans[i][1]+1)