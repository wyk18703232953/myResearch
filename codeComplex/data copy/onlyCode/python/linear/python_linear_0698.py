n, v = map(int, raw_input().split())

res=0
fuel=0
for i in range(1,n):
    miss = min(v-fuel, n-i-fuel)
    res+=i*miss
    fuel+=miss-1
    if v-fuel==0:
        print(res)
        exit(0)
print(res)