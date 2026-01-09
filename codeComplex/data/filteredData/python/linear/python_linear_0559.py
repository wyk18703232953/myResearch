def add(num):
    if num <= 1:
        return 0
    return (num * (num - 1)) // 2

def solve(a, k):
    n = len(a)
    pre = [a[0]]
    base = (1 << k) - 1
    hb = 1 << (k - 1)

    for i in range(1, n):
        pre.append(a[i] ^ pre[-1])

    cnt = {}
    cnt[0] = [0, 0]

    for i in range(n):
        if pre[i] >= hb:
            key = base - pre[i]
            if key not in cnt:
                cnt[key] = [0, 0]
            cnt[key][1] += 1

        else:
            key = pre[i]
            if key not in cnt:
                cnt[key] = [0, 0]
            cnt[key][0] += 1

    cnt1 = 0
    for v in cnt.values():
        s = v[0] + v[1]
        cnt1 += add(s // 2)
        cnt1 += add((s + 1) // 2)
    cnt1 += sum(cnt[0]) // 2

    return (n * (n + 1)) // 2 - cnt1

def main(n):
    # 生成测试数据：
    # 选取 k 使得数值规模合理，例如 k = 3
    k = 3
    # 生成一个长度为 n 的数组，元素为 [0, 2^k-1] 内的整数
    a = [(i * 7 + 3) % (1 << k) for i in range(n)]

    ans = solve(a, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)