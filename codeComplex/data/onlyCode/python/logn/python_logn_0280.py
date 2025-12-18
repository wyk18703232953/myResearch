sp = 10**9 + 7;

def power(number,n):
    res = 1
    while(n != 0):
        if n % 2 != 0:
            res *= number
            res %= sp
            n-= 1
        number *= number
        number %= sp
        n //= 2
    return res % sp


x,k = map(int,input().split())
if x == 0:
    print(0)
else:
    print(((((x % sp) * (power(2,k)))%sp*2)%sp - ((power(2,k)-1))%sp ) % sp)
