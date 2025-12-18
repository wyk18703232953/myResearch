def mul(a, b, md) :
    if(b == 1) :
        return a
    if(b % 2 == 0) :
        t = mul(a, b // 2, md)
        return (2 * t) % md
    return (mul(a, b - 1, md) + a) % md;

def pows(a, b, md) :
    if(b == 0) :
        return 1
    if(b % 2 == 0) :
        t = pows(a, b // 2, md)
        return mul(t, t, md) % md
    return (mul(pows(a, b - 1, md) , a, md)) % md;


x, k = map(int, input().split())
ch = pows(2, k, 1000000007)
ans = pows(2, k + 1, 1000000007) * x - ch + 1
ans = ans % (1000000007)
if(x == 0) : 
    ans = 0
print(ans)