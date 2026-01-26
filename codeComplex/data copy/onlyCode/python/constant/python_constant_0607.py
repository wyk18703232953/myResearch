n, k = map(int, input().split())
print((n*2)//k + bool((n*2)%k) + (n*5)//k + bool((n*5)%k) + (n*8)//k + bool((n*8)%k))