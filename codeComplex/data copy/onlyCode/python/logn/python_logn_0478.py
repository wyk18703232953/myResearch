k = int(input())
a = 9
for i in range(1,12):
    if k<=a*i:
        a = (a//9)+(k//i)-1
        if k%i!=0:
            b = str(a+1)
            c = (k%i)-1
            print(b[c])
        else:
            b = str(a)
            print(b[-1])
        break
    else:
        k = k-a*i
        a = a*10
