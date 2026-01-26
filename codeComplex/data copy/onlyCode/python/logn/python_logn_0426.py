def pow(x, p):
    ret = 1
    for i in range(p): ret=ret*x
    return ret

def rate(p):
    ret = 0
    now = 1
    for i in range(p):
        ret = ret + now
        now = now * 4
    return ret

def solve():
    n, k = map(int, input().split())
    if (n>35):
        print("YES %d" % (n-1))
        return 
    mSplit = 1
    cnt1 = 0 
    cnt3 = 1
    for i in range(1, n+1):
        now = pow(4, i) - pow(2, i+1) + 1
        now = now * rate(n-i) + rate(i)
        # print("%d %d %d %d"%(n, i, now, mSplit))
        if (k<=now):
            print("YES %d" % (n-i))
            return
        mSplit = mSplit + cnt1 + cnt3 * 3
        cnt1 = cnt1 + cnt3
        cnt3 = cnt3 + cnt3
        if (mSplit>k): break
    print("NO")


def main():
    T = int(input())
    for i in range(T): 
        solve()

if __name__ == "__main__":
    main()
