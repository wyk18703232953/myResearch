def main(n):
    # 映射含义：
    # n: 字典键的规模（原程序中的 n）
    # m: 序列长度，这里设为 n 的平方，以便放大时间复杂度
    # 序列 li: 使用确定性构造 (i % n) + 1 得到 1..n 的循环序列
    if n <= 0:
        print(0)
        return

    m = n * n  # 可根据需要调整为其他与 n 相关的确定性规模
    li = [(i % n) + 1 for i in range(m)]

    dic = {}
    c = 0
    for i in range(n):
        dic.setdefault(i + 1, 0)
    for i in li:
        if 0 not in dic.values():
            c = c + 1
            for j in range(1, n + 1):
                dic[j] = dic[j] - 1

        dic[i] = dic[i] + 1
    if 0 not in dic.values():
        c = c + 1
    print(c)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值来做规模实验
    main(5)