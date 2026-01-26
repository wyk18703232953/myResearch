arra = []
arrb = []
arr = []
s = ""
temp = 1 
value = ans = n = 0
 
def fill(myList = [], *args):
    for i in range(n):
        arra.insert(0,0)  
        
def check():
    for i,j in zip(arra,arrb):
        if i == j:
            return 1
        else:
            return 0

        
def Engine1(num): 
    if num > 1: 
        Engine1(num // 2) 
    arra.append( num%2 )
def Engine2(num):
    if num > 1: 
        Engine2(num // 2) 
    arrb.append( num%2 )

a,b = map(int,input().split())
Engine1(a)
Engine2(b)

n = abs(len(arra)-len(arrb))
if(len(arra)>len(arrb)):
    fill(arrb)
if(len(arra)<len(arrb)):
    fill(arra)
    

for i in range(len(arra)):
    if(check() == 0):
        break
    check()
    arra.pop(0)
    arrb.pop(0)

for i in range(len(arra)):
    ans += temp
    temp *= 2
print(ans)