from sys import stdout
from sys import stdin
def get():
    return stdin.readline().strip()
def getf(sp = " "):
    return [int(i) for i in get().split(sp)]
def put(a, end = "\n"):
    stdout.write(str(a) + end)
def putf(a, sep = " ", end = "\n"):
    stdout.write(sep.join([str(i) for i in a]) + end)
   
#from collections import defaultdict as dd, deque
#from random import randint, shuffle, sample
#from functools import cmp_to_key, reduce
#from math import factorial as fac, acos, asin, atan2, gcd, log, e
#from bisect import bisect_right as br, bisect_left as bl, insort

from math import log
from bisect import bisect_right as br, bisect_left as bl

def main():
    n, k = getf()
    a = getf()
    rem = [[] for i in range(11)]
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
            if(l > sz - 1):
                continue
            if(rem[add_len][l] == need_rem):
                res += (r - l)
        if((a[i] + (a[i] % k) * pow(10, ln[i], k)) % k == 0):
            res -= 1
        ans += res
    put(ans)
main()
