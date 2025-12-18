s = input().split(' ')
s1 = s[0]
s2 = s[1]
res = s1[0]
flag = 0
for i in range(1, len(s1)):
    if(s1[i]>=s2[0]):
        res+=s2[0]
        flag = 1
        break
    else:
        res+=s1[i]
if(flag == 0):
    res+=s2[0]
print(res)
