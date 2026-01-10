from math import log
from bisect import bisect_right as br, bisect_left as bl

def main(n):
    if n <= 0:
        return
    k = max(1, n // 2)
    a = [i + 1 for i in range(n)]
    rem = [[] for _ in range(11)]
    ln = [0] * n
    for i in range(n):
        ln[i] = int(log(a[i], 10)) + 1
        rem[ln[i]] += [a[i] % k]
    for i in range(11):
        rem[i].sort()
    ans = 0
    for i in range(n):
        res = 0
        for add_len in range(1, 11):
            cur_rem = ((a[i] % k) * pow(10, add_len, k)) % k
            need_rem = (k - cur_rem) % k
            sz = len(rem[add_len])
            l = bl(rem[add_len], need_rem)
            r = br(rem[add_len], need_rem)
            if l > sz - 1:
                continue
            if rem[add_len][l] == need_rem:
                res += (r - l)
        if (a[i] + (a[i] % k) * pow(10, ln[i], k)) % k == 0:
            res -= 1
        ans += res
    print(ans)

if __name__ == "__main__":
    main(10)