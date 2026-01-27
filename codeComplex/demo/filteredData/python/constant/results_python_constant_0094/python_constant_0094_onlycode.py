for _ in range(int(input())):
    a,b = map(int, input().split())
    c = 0
    while (a!=0 and b!=0):
        if (a>b) : 
            c+= a//b
            a = a%b
        elif (b>a):
            c+= b//a
            b = b%a
        else :
            c+=1
            break
    print(c)