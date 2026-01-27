def numz(a, b):
    if a and b:
        if b > a:
            a, b = b, a
        d, m = divmod(a, b)
        return d + numz(b, m)

    else:
        return 0


def main(n):
    # 模拟原程序的输入结构：
    # 第1行：一个整数，表示后续行数（这里设为 n）
    # 接下来 n 行：每行两个整数，对应 numz 的输入
    #
    # 为了可规模化和确定性生成数据：
    # 第 i 行（从 0 到 n-1）生成一对 (a, b)，例如：
    # a = i + 1
    # b = (2*i + 1) 或者至少为 1，避免全为 0。
    #
    # 为了保证对任意 n > 0 有意义的调用，且避免 b 为 0：
    # a_i = i + 1
    # b_i = i // 2 + 1

    results = []
    for i in range(n):
        a = i + 1
        b = i // 2 + 1
        results.append(numz(a, b))

    # 模拟原程序的输出行为：逐行打印结果
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行不同规模的实验
    main(10)