import sys
input = sys.stdin.readline
 
n = int(input())
li = []
 
for i in range(n):
    x,w = map(int,input().split())
    li.append((x-w,x+w))
 
li.sort(key = lambda x: x[1])
 
a = -10 ** 9
ans = 0
 
for i in range(n):
     if a <= li[i][0]:
         ans += 1
         a = li[i][1]
 
print(ans)