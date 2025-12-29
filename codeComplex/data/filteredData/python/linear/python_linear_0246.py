def main(n: int):
    # 生成测试数据：按照题意构造一个合理的 k
    # 示例策略：
    #   - n < 3 时，k 只能非常小，这里统一设为 min(2, n)
    #   - n >= 3 时，让 k 在 [0, 2n] 内变化，这里用 k = n，兼顾偶数/奇数两种情况
    if n <= 0:
        return
    if n < 3:
        k = min(2, n)
    else:
        k = n

    if k % 2 == 0:
        s = "."
        s = s + "#" * (k // 2)
        s = s + "." * (n - len(s))
        print("YES")
        print("." * n)
        print(s)
        print(s)
        print("." * n)
    else:
        if k <= n - 2:
            a = "#" * k
            s = "." * ((n - k) // 2) + a + "." * ((n - k) // 2)
            print("YES")
            print("." * n)
            print(s)
            print("." * n)
            print("." * n)
        else:
            k = k - n + 3
            a = "#" * k
            s = "." * ((n - k) // 2) + a + "." * ((n - k) // 2)
            print("YES")
            print("." * n)
            print("." + "#" * (n - 2) + ".")
            s = list(s)
            s[n // 2] = "."
            s = "".join(s)
            print(s)
            print("." * n)


if __name__ == "__main__":
    # 示例调用：可以在此修改 n 的大小进行测试
    main(7)