# %matplotlib inline

def main():
    n, k = [int(x) for x in input().split(' ')]
    if k==1:
        print(n)
        return
    a = []
    b = {}
    a = [int(x) for x in input().split(' ')]
    a.sort()

    a=dict(zip(a,range(n)))
    count = {}

    for x in a:
        if x % k == 0 and int(x / k) in a:
            b[x] = b[int(x / k)]
            count[b[int(x / k)]] += 1
        else:
            b[x] = x
            count[x] = 1

    for x,y in count.items():
        n -= int(y / 2)

    print(n)


main()
