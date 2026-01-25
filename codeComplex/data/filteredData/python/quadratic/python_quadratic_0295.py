def main(n):
    # n 表示数组长度（必须为偶数，若为奇数则减一）
    if n < 2:
        print(0)
        return
    if n % 2 == 1:
        n -= 1

    # 与原程序 input 一致：代码中使用的是 2 * int(input())
    # 这里直接使用 n 作为长度，因此不再乘 2
    a = [(i // 2) for i in range(n)]  # 构造确定性数组，可含重复元素
    z = 0

    i = 0
    while i < n - 1:
        if a[i] != a[i + 1]:
            j = i + 1
            while j < n:
                if a[j] == a[i]:
                    z += j - i - 1
                    val = a.pop(j)
                    a.insert(i + 1, val)
                    n -= 0  # n 实际长度保持一致逻辑，无需更新循环上界用到的表达式
                    break
                j += 1
        i += 2

    print(z)


if __name__ == "__main__":
    main(10)