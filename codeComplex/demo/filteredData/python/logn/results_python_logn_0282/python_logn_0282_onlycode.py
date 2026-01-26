import sys, math
debug = 0
if debug:
    f = open("input.txt", "r")
    input = f.readline
def mp():
    return list(map(int,input().split()))

m = 1000000007    

def pow(k):
    if k == 0:
        return 1;
    z = pow(k // 2)
    if k % 2 == 1:
        return (2 * z * z) % m
    else:
        return (z * z) % m
        
def _main():
    x, k = mp()
    if(x == 0):
        print(0)
        return
    t = pow(k)
    a = x * t
    b = a - t + 1;
    print((a + b) % m)
    
     
_main()