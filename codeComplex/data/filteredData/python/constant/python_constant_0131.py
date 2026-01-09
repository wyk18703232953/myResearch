def main(n):
    # 解释：这里将输入规模 n 映射为 (A, B) 两个正整数
    # 使用简单的确定性规则构造：
    # A = n + 1
    # B = n // 2 + 1  (确保 B >= 1)
    A = n + 1
    B = n // 2 + 1

    a = 0
    while B:
        a += A // B
        A, B = B, A % B
    # print(a)
    pass
if __name__ == "__main__":
    # 示例：可以根据需要修改 n 以改变规模
    main(10)