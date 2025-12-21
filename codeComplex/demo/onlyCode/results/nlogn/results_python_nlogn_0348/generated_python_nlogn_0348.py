from collections import defaultdict
import random

def main(n):
    a = [random.randint(0, 1000000000) for _ in range(n)]
    pow2 = [1 << i for i in range(32)]
    mp = defaultdict(int)
    for x in a:
        mp[x] = 1
    mxSiz = 1
    ans = [a[0]] if a else []
    for x in a:
        for y in pow2:
            if x - y in mp and x + y in mp:
                mxSiz = 3
                ans = [x - y, x, x + y]
            if x - y in mp and 2 > mxSiz:
                mxSiz = 2
                ans = [x - y, x]
    print(mxSiz)
    print(*ans)
    return mxSiz, ans

if __name__ == "__main__":
    main(10)