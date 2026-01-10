def main(n):
    # 为了保持与原程序结构一致，我们需要 n 和 k，以及长度为 n 的数组 a
    # 这里将规模 n 映射为数组长度，k 设为与 n 有关联的确定性值
    if n <= 0:
        print(0)
        return

    k = max(2, (n % 10) + 2)  # 确定性地生成 k，且保证 k >= 2

    # 确定性生成长度为 n 的数组 a
    # 使用简单的算术构造，让数据有一定离散性和重复性
    a = [(i * 3 + (i // 2) + k) for i in range(n)]
    a = sorted(a)

    s = set()
    for i in range(n):
        if a[i] % k != 0:
            s.add(a[i])
        elif a[i] // k not in s:  # 使用整除，对应原代码的 a[i] / k（在整数上下文中）
            s.add(a[i])
    print(len(s))


if __name__ == "__main__":
    # 示例调用，用于规模化实验时可修改此处的 n
    main(10)