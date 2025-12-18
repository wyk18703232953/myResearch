n, k = map(int,input().split())
s = input()
p = len(s)-1
while s[:p] != s[-p:]:
    p =  p -1
print(s + s[p:]*(k-1))