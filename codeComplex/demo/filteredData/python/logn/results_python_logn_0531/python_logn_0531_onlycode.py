k=int(input())

s=0
i=1
while  (s +  i * ( 9 * pow ( 10,i-1)) ) < k :
    s +=  i * (9 * pow(10, i - 1))
    i+=1
else:
    i-=1

k=k-s-1
x= k // (i+1)
y= k %(i+1)
x= pow(10,i)+x
ss=str(x)
print(ss[y])
