import bisect
from collections import defaultdict as dd
import random


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
            for _ in range(d[i]):
                if i == 0:
                    co += 1
                    if co > r:
                        break
                ans += str(i)

    print(ans)


def main(n):
    # 生成长度为 n 的 s1 和 s2（每位是 0-9 的数字）
    # 保证两串非空且长度分布类似原逻辑
    length_s1 = n
    # s2 长度在 [n-2, n+2] 范围内随机选取，至少为 1
    length_s2 = max(1, n + random.randint(-2, 2))

    s1 = [random.randint(0, 9) for _ in range(length_s1)]
    s2 = [random.randint(0, 9) for _ in range(length_s2)]

    z = s1.count(0)
    d = dd(int)
    n_len = len(s1)
    m_len = len(s2)
    l = sorted(s1)
    for x in s1:
        d[x] += 1

    if len(s1) < len(s2):
        # 原代码：直接输出从大到小的排列
        ans = "".join(str(l[i]) for i in range(len(s1) - 1, -1, -1))
        print(ans)
    elif len(s1) > len(s2):
        r = m_len - (n_len - z)
        l2 = l[z - r:]
        solve(l2, d, s2, r)
    else:
        solve(l, d, s2, 100)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)