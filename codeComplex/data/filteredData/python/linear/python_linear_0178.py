import random

def main(n, k=None, seed=0):
    """
    n: 规模，表示数组长度
    k: 滑窗长度；若为 None，则自动设置为 max(1, n // 3)
    """
    random.seed(seed)

    # 若调用者未指定 k，则给一个与 n 相关的值
    if k is None:
        k = max(1, n // 3)
    k = min(k, n)  # 保证 k 不超过 n

    # 生成测试数据：
    # a: 随机正整数
    # t: 0/1 标记
    a = [random.randint(1, 10) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]

    # 以下为原逻辑
    ans = sum(a[ii] for ii in range(n) if t[ii])
    bb = [a[ii] if t[ii] == 0 else 0 for ii in range(n)]

    if k == 0:
        print(ans)
        return

    ll = 0
    rr = k
    sws = sum(bb[:k])
    tmp = sws

    while rr < n:
        sws -= bb[ll]
        sws += bb[rr]
        ll += 1
        rr += 1
        tmp = max(tmp, sws)

    ans += tmp
    print(ans)


if __name__ == "__main__":
    # 示例：n=10，窗口长度自动选择
    main(10)