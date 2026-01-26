n = int(input())

m = input()

s = list(m)

if n==1:
    ans = s[0]
else:
    count = 0
    for i in range(0,n):
        if s[i]=='0':
            count = count + 1
    ans = '1'
    for i in range(0,count):
        ans = ans + '0'

print(ans)