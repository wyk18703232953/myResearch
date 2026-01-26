def f(l,r,g,b,op):
    if (r==0 and g==0) or (r==0 and b==0) or (b==0 and g==0):
        return 0
    else:
        if op[r][g][b]!=-1:
            return op[r][g][b]
        if r==0:
           op[r][g][b]=l[1][g-1]*l[2][b-1]+f(l,r,g-1,b-1,op)
           return op[r][g][b]
        if g==0:
           op[r][g][b]=l[0][r-1]*l[2][b-1]+f(l,r-1,g,b-1,op)
           return op[r][g][b]
        if b==0:
         op[r][g][b]=l[0][r-1]*l[1][g-1]+f(l,r-1,g-1,b,op)
         return op[r][g][b]
        op[r][g][b]=max(l[1][g-1]*l[2][b-1]+f(l,r,g-1,b-1,op),l[0][r-1]*l[2][b-1]+f(l,r-1,g,b-1,op),l[0][r-1]*l[1][g-1]+f(l,r-1,g-1,b,op))  
        return op[r][g][b]   

r,g,b=list(map(int,input().split()))
l=[]
l.append(sorted(list(map(int,input().split()))))
l.append(sorted(list(map(int,input().split()))))
l.append(sorted(list(map(int,input().split()))))
op=[[[-1 for i in range(b+1)]for j in range(g+1)]for k in range(r+1)]
#print(op)
print(f(l,r,g,b,op))
