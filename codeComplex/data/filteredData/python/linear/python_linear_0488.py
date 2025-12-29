from collections import defaultdict
import random


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(n):
    # 生成规模为 n 的测试数据：n 个区间 [l, r]
    # 保证所有区间合法且至少有 1 个区间
    if n <= 0:
        n = 1

    lst = []
    for _ in range(n):
        # 生成随机区间，范围可调整
        l = random.randint(0, 1000)
        r = random.randint(l, l + random.randint(0, 1000))
        lst.append([l, r])

    d = defaultdict(int)
    ll = defaultdict(list)
    rr = defaultdict(list)
    llst = []
    rlst = []

    for l, r in lst:
        llst.append(l)
        rlst.append(r)
        ll[l].append(r)
        rr[r].append(l)

    left = max(llst)
    right = min(rlst)
    lleft = min(ll[left])
    lright = max(rr[right])

    lst.remove([left, lleft])
    pl = max(i[0] for i in lst)
    pr = min(i[1] for i in lst)
    mx = max(0, pr - pl)

    lst.append([left, lleft])
    lst.remove([lright, right])
    pl = max(i[0] for i in lst)
    pr = min(i[1] for i in lst)

    ans = max(mx, max(0, pr - pl))
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 个区间并运行逻辑
    main(5)