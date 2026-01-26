def main(n):
    # 通过 n 确定性生成输入 n, p, l, r
    # 设:
    #   N = max(1, n)
    #   p = (2 * n) % N + 1
    #   l = (n // 3) % N + 1
    #   r = (2 * n // 3) % N + 1
    # 并强制 1 <= l <= r <= N，且 p 也被限制在 [1, N]
    N = max(1, n)

    p = (2 * n) % N + 1
    l = (n // 3) % N + 1
    r = (2 * n // 3) % N + 1

    # 规范化区间
    if l > r:
        l, r = r, l

    # 保证 r 不超过 N
    if r > N:
        r = N
    if l > r:
        l = r

    # 保证 p 在 [1, N]
    if p > N:
        p = N

    # 原始逻辑
    if l == 1 and r == N:
        ans = 0
    elif l == 1:
        ans = abs(p - r) + 1
    elif r == N:
        ans = abs(p - l) + 1

    else:
        ans = min(abs(p - r), abs(p - l)) + r - l + 2

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)