def main(n):
    # 这里根据 n 生成测试数据：
    # 为了更有代表性，构造几种不同情况：
    # 1) 全不同且不可通过 &x 变为已有元素 → 输出 -1
    # 2) 存在 a[i]&x == 其他元素且 v!=a[i] → 输出 1
    # 3) 存在重复 → 输出 0
    #
    # 你可以根据需要替换生成逻辑，这里给出一个简单示例：
    if n <= 2:
        # 小规模手动构造示例
        x = 3
        a = list(range(1, n + 1))

    else:
        # 构造一个一般情况：
        # a = [1, 2, ..., n]
        # 并选择一个 x，使得某些位操作有机会改变结果
        x = (1 << 20) - 1  # 一个较大的掩码
        a = list(range(1, n + 1))

    # 以下为原逻辑移植，只去掉了 input/输出控制
    s = set(a)
    if len(s) != n:
        # print(0)
        pass
        return

    ans = 0
    b = a[:]  # 拷贝以便与原值比较
    for i in range(n):
        v = b[i]
        b[i] &= x
        if b[i] in s and v != b[i]:
            ans = 1
            break

    if ans == 1:
        # print(1)
        pass
    elif len(set(b)) == n:
        # print(-1)
        pass

    else:
        # print(2)
        pass
if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)