n=int(input())
if n>-1:
    print(n)
else:
    n=str(n)
    x=int(n[:len(n)-1])
    y=int(n[:len(n)-2]+n[-1])
    print(max(x,y))