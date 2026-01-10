def main(n):
    # 映射意义：
    # n -> 列表 a1 的长度
    # n, m, k 三个值由 n 确定性生成
    # 保持算法逻辑不变

    # 生成 n, m, k
    n_val = n
    m = 2 * n_val + 5
    k = n_val // 2

    # 生成 a1 列表，长度为 n_val，元素为确定性整数
    # 使用简单算术序列：i % 7 + 1，保证正整数且有重复
    a1 = [(i % 7) + 1 for i in range(n_val)]

    # 对应原代码逻辑
    a1 = list(sorted(a1))

    count = 0
    for i in range(len(a1)):
        if k >= m:
            break
        else:
            k += a1.pop() - 1
            count += 1

    if k >= m:
        print(count)
    else:
        print("-1")


if __name__ == "__main__":
    main(10)