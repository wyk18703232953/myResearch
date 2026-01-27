n=int(input())
c=0
lst=[4,7,47,74,447,474,744,477,747,774]
if n in lst:
    print("YES")
else:
    for i in lst:
        if n%i==0:
            print("YES")
            c=c+1
            break
        else:
            continue
    if c==0:
        print("NO")
    
