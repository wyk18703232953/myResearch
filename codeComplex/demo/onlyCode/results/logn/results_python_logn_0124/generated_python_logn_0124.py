f = lambda m, k: (k * m - m * (m - 1) // 2 - m + 1)

def ok(m, k, n):
    return f(m, k) >= n

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序需要 n, k，这里令 k 与 n 同阶，例如 k = n
    k = n

    if not ok(k, k, n):
        print(-1)
        return

    l, h = 0, k
    while h > l:
        mid = l + (h - l) // 2
        if ok(mid, k, n):
            h = mid
        else:
            l = mid + 1
    print(h)


if __name__ == "__main__":
    # 示例：调用 main(n)，外部可自行调整 n 的值
    main(10)