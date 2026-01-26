def bina(bi):    
    binary1 = bi 
    decimal, i, n = 0, 0, 0
    while(bi != 0): 
        dec = bi % 10
        decimal = decimal + dec * pow(2, i) 
        bi = bi//10
        i += 1
    return decimal
def con(n):
   return bin(n).replace("0b", "")
l,r=map(int,input().split())
k=con(l)
m=con(r)
k=list(str(k))
m=list(str(m))
j=len(m)-len(k)
k=['0']*j + k
#print(*k,sep='')
#print(*m,sep='')
c=0
for i in range(len(m)):
    if k[i]!=m[i]:
        c=1
    if k[i]==m[i] and k[i]=='1' and c==1:
        k[i]='0'
    elif k[i]==m[i] and k[i]=='0' and c==1:
        k[i]='1'          
k=int(''.join(k))
m=int(''.join(m))
print(bina(k)^bina(m))           