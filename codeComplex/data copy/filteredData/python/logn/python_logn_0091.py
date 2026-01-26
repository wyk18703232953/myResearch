def main(n):
    # 解释输入结构：
    # 原程序读取两个整数 a, b
    # 这里用 n 的比特模式构造一个“接近但不同”的 b
    # 保证：当 n > 0 时，a != b；当 n == 0 时，a == b
    a = n
    if n == 0:
        b = 0

    else:
        # 将 n 的最低位翻转，保证 a != b 且规模随 n 变化
        b = n ^ 1

    idx = 0
    if a == b:
        # print(0)
        pass

    else:
        for i in range(63, -1, -1):
            set1 = (a >> i) & 1
            set2 = (b >> i) & 1
            if set1 != set2:
                idx = i
                break
        # print((1 << (idx + 1)) - 1)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模化实验
    main(10)