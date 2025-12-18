a,b = map(int,input().split())
ans = 0
if(a > b):
    ans += int(a//b)
    a = a%b
while(b!=0):
    ans += int(a//b)
    a,b = b,a%b
print(ans)