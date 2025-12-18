s=input()
c=c1=0
for i in range(len(s)//2):
    if s[i]==s[len(s)-i-1]:
        c+=1
for i in range(len(s)):
    if s[i]==s[0]:
        c1+=1
if c1==len(s):
    print(0)
elif c==len(s)//2:
    print(len(s)-1)
else:
    print(len(s))