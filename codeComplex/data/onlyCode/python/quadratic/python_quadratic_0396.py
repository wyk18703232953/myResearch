n,m=input().split()
i=j=-1
while(j<0):
    mat=input()
    j=mat.find('B')
    i+=1
    c=mat.count('B')//2+1
print(i+c,j+c)