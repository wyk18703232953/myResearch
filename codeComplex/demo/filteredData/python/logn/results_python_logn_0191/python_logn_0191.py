def main(n):
    # 解释：原程序读入 n, k，这里我们把规模参数 n 映射为原来的 n，
    # 并确定性构造 k，使得随着规模增大，k 也有合理变化。
    # 这里选取一个确定性的线性关系：k = max(1, n // 3)
    k = n // 3
    if k <= 0:
        k = 1

    x, y = 1, n
    f = 0
    m = 0  # 需要在循环外先定义，保证后续使用安全

    while x <= y:
        m = (x + y) // 2

        # 计算 m 的数位和
        s = 0
        p = m
        while p > 0:
            s += p % 10
            p //= 10

        # 计算 m-1 的数位和
        m1 = m - 1
        s1 = 0
        p = m1
        while p > 0:
            s1 += p % 10
            p //= 10

        if m == 0 or (m - s >= k and m1 - s1 < k):
            f = 1
            break
        elif m - s < k:
            x = m + 1

        else:
            y = m - 1

    if f:
        # print(n - m + 1)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以进行不同规模实验
    main(10**6)