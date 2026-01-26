s = input()
one = s.count('1')
zero = 0
ind = -1
for i in range(len(s)):
    if s[i]=='2':
        ind=i
        break
    if s[i]=='0':
        zero+=1
d = ""
if ind==-1:
    print("0"*zero+"1"*one)
    exit()
d =  d + "0"*zero+"1"*one
for i in s[ind:]:
    if i!='1':
        d+=i
print(d)        
        
    
