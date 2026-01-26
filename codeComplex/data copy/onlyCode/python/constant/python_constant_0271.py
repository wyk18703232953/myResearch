x=list(map(int,input().split()))
pos=x[1]
n=x[0]
l=x[2]
r=x[3]
step=0
if pos<l :
    step=l-pos+1
    
    if r< n :
        step+=r-l+1
elif pos>r:
    step=pos-r+1
    
    if l> 1 :
        step+=r-l+1
else:
    if l>1 and n>r:
        step+=min(pos-l,r-pos)+r-l+2
    elif l==1 and n>r:
        step=r-pos+1
    elif l>1 and n==r:
        step+=pos-l+1
    else:
        step=0



print(step)