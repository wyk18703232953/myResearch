n=int(input())
s=input()

h=s.count('H')
s=s+s
print(min(s[i:i+h].count('T') for i in range(n)))
