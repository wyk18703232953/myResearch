def main(n: int):
    # 生成测试数据：
    # 模拟一种合理场景：
    # pos 在 [1, n] 范围内
    # l, r 为一个区间 [l, r]，1 <= l <= r <= n
    # 这里给出一个简单的构造方式：让 pos 在区间中间附近，区间长度约为 n//2
    if n <= 0:
        return

    # 简单构造：区间长度 len_seg，pos 在区间中点
    len_seg = max(1, n // 2)
    l = 1
    r = min(n, l + len_seg - 1)
    pos = (l + r) // 2

    dl = abs(pos - l) + 1
    dr = abs(pos - r) + 1
    ans = dr * (r < n) if l == 1 else dl if r == n else min(dl, dr) + r - l + 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)