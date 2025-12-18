n,k = map(int,input().split())
s = input()
c=0
for i in range(len(s)):
	if s[:i]==s[-i:]:
		c=i
print(s+s[c:]*(k-1))