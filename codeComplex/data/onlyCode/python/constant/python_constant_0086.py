def NOD(a, b):
    while b != 0:
        a %= b
        y = a
        a = b
        b = y
    return(a)
    
def NOK(a, b):
    i = (a*b) // NOD(a, b)
    return(i)
 
 
n = int(input())
maxnok = 0
x = 40
for i in range(max(1, n-x), n+1):
    for j in range(max(1, i-x), i+1):
        for f in range(max(1, j-x), j+1):
            nokk = NOK(NOK(i,j), f)
            if maxnok < nokk:
                maxnok = nokk
                delit = []
                delit.append(i)
                delit.append(j)
                delit.append(f)
print(maxnok)