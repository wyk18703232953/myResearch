a=str(input())
b=str(input())
count=0
al=len(a)
bl=len(b)
s=b[:bl-al+1].count('1')
for i in range(al-1):
    if a[i]=='0':
        count+=s
    else:
        count+=bl-al+1-s
    s+=int(b[bl-al+i+1])-int(b[i])
 
if a[-1]=='0':
    count+=s
else:
    count+=bl-al+1-s
print(count)