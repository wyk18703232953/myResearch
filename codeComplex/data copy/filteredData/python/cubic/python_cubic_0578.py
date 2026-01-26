import bisect
from collections import defaultdict as dd

def solve(l, d, s2, r):
    ans = ""
    lol = 0
    i = 0
    lo = 0
    while i < len(s2):
        if lo == 1:
            a = s2[i]
            ind = bisect.bisect_left(l, a)
            for x in range(ind, -1, -1):
                if l[x] < l[ind]:
                    ind = x
                    break
            ans += str(l[ind])
            d[l.pop(ind)] -= 1
            lol = 1
            break

        a = s2[i]
        ind = bisect.bisect_left(l, a)

        if ind == len(l):
            ind -= 1
            ans += str(l[ind])
            d[l[ind]] -= 1
            lol = 1
            break
        elif l[ind] > a:
            if ind == 0:
                while ind == 0:
                    l.append(int(ans[-1]))
                    d[int(ans[-1])] += 1
                    l.sort()
                    ans = ans[:len(ans) - 1]
                    lo = 1
                    i -= 1
                    a = s2[i]
                    ind = bisect.bisect_left(l, a)
                continue
            lol = 1
            ans += str(l[ind - 1])
            d[l[ind - 1]] -= 1
            l.pop(ind - 1)
            break

        else:
            ans += str(l[ind])
            d[l[ind]] -= 1
            l.pop(ind)
        i += 1
    ll = []
    if lol:
        for i in d:
            if d[i] != 0:
                ll.append(i)
        ll.sort(reverse=True)
        co = 0
        for i in ll:
            for j in range(d[i]):
                if i == 0:
                    co += 1
                    if co > r:
                        break
                ans += str(i)
    # print(ans)
    pass


def main(n):
    # Deterministic generation of s1 and s2 based on n
    # s1 length = n, s2 length = n (to cover main branches)
    # digits of s1 and s2 are in [0..9] generated deterministically
    s1 = [(i * 3 + 1) % 10 for i in range(n)]
    s2 = [(i * 5 + 2) % 10 for i in range(n)]

    z = s1.count(0)
    d = dd(int)
    length_s1 = len(s1)
    length_s2 = len(s2)
    l = sorted(s1)
    for i in s1:
        d[i] += 1

    if len(s1) < len(s2):
        for i in range(len(s1) - 1, -1, -1):
            # print(l[i], end="")
            pass
        # print()
        pass
    elif len(s1) > len(s2):
        r = length_s2 - (length_s1 - z)
        l = l[z - r:]
        solve(l, d, s2, r)

    else:
        solve(l, d, s2, 100)


if __name__ == "__main__":
    main(1000)