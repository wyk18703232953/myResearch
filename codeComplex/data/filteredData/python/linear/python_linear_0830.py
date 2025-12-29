def solve(d, n, k):
    mv = sum(d[0:k])
    v = mv
    for i in range(1, n - k + 1):
        mv = mv + d[i + k - 1] - d[i - 1]
        v = min(v, mv)
    return v

def main(n):
    # 生成测试数据
    # 这里根据 n 构造字符串 s 和窗口大小 k
    # 用户可按需要自行修改这一部分的生成逻辑
    k = max(1, n // 2)  # 示例：令 k 为 n 的一半（向下取整，至少为 1）
    import random
    chars = ['R', 'G', 'B']
    s = ''.join(random.choice(chars) for _ in range(n))

    st = 'RGB' * (n // 3 + 3)
    diff1, diff2, diff3 = [0] * n, [0] * n, [0] * n

    for i in range(n):
        if s[i] != st[i]:
            diff1[i] = 1
        if s[i] != st[i + 1]:
            diff2[i] = 1
        if s[i] != st[i + 2]:
            diff3[i] = 1

    ans = min(
        solve(diff1, n, k),
        solve(diff2, n, k),
        solve(diff3, n, k)
    )
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此调整
    main(10)