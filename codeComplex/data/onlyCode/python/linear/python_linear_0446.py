import math
#t=int(input())
#for i in range(t):
n,m = map(int, input().strip().split(' '))
#lst = list(map(int, input().strip().split(' ')))
s=input()
t=input()
if '*' not in s:
    if s==t:
        print('YES')
    else:
        print('NO')
elif n>m+1:
    print('NO')
elif n==1 and s=='*':
    print('YES')
else:
    s=list(s)
    t=list(t)
    if s[0]=='*':
        if s[1:]==t[-(len(s[1:])):]:
            print('YES')
        else:
            print('NO')
    elif s[-1]=='*':
        if s[:n-1]==t[:n-1]:
            print('YES')
        else:
            print('NO')
    else:
        ind=s.index('*')
        #print(ind)
        #print(s[ind+1:])
        #print(t[-len(s[ind+1:]):])
        if s[:ind]==t[:ind] and s[ind+1:]==t[-len(s[ind+1:]):]:
            print('YES')
        else:
            print('NO')
        

