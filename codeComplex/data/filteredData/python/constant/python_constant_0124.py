def main(n):
    # 原程序逻辑：对单个整数 n 进行处理
    if n >= 0:
        # print(n)
        pass

    else:
        n_abs = -n
        rem = n_abs % 10
        n1 = n_abs // 10
        n2 = n1 // 10
        n2 = n2 * 10 + rem
        k = min(n1, n2)
        # print(-k)
        pass
if __name__ == "__main__":
    # 示例：以 n 为输入规模，构造一个确定性的整数作为原程序输入
    # 这里选择将输入规模 n 映射为整数 x = n*(-1)**n
    # 这样 n 控制数值大小，且正负交替，便于实验
    x = (10 * n if (n := 10) >= 0 else -10)  # 固定示例：规模 10，对应输入 100 或 -100 等
    # 为了符合要求，示例调用使用固定规模 10
    main(x)