x, k = map(int, input().split())

if x == 0:
    result = 0
else:
    modulo = 10**9 + 7
    
    x %= modulo
    
    result = pow(2, k, modulo)*(2*x - 1) + 1
    result %= modulo

print(result)