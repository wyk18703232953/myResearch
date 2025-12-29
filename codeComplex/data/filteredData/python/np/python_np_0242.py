import random

def main(n):
    # 生成测试数据
    # 约束范围可以根据需要调整
    l = 10
    r = 100
    x = 5

    # 生成 n 个正整数作为数组 a
    a = [random.randint(1, 30) for _ in range(n)]

    cnt = 0

    for i in range(0, 1 << n):
        s = 0
        mn = int(1e18)
        mx = 0

        for j in range(0, n):
            if (i >> j) & 1:
                s += a[j]
                mn = min(mn, a[j])
                mx = max(mx, a[j])

        if l <= s <= r and (mx - mn) >= x:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(5)