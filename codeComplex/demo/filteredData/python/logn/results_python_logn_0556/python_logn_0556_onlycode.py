k = int(input())

for i in range(20):
    if k > 10**i * 9 * (i+1):
        k -= 10**i * 9 * (i+1)
    else:
        a, b = (k-1) // (i+1) + 10**i, (k-1) % (i+1)
        print(str(a)[b])
        break