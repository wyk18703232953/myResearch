from math import log
from bisect import bisect_right as br, bisect_left as bl
from random import randint

def main(n):
    # 1. 生成测试数据
    # 约束：a[i] >= 1，k >= 1
    # 随机生成 k，避免为 0
    k = randint(1, 10**9)
    # 随机生成数组 a，元素为 1 到 10^9 之间的整数
    a = [randint(1, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    rem = [[] for _ in range(11)]
    ln = [0] * n
    for i in range(n):
        ln[i] = int(log(a[i], 10)) + 1
        rem[ln[i]].append(a[i] % k)
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
    # 示例：调用 main，n 为规模参数
    main(5)