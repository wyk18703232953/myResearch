def main(n):
    # 解释原程序的输入含义：
    # 原始程序读取 n, m，接着在 1..n 上循环
    # 这里我们将实验规模参数 n 映射为原程序中的 n
    # 并构造一个与 n 有确定关系的 m，保证可规模化且确定性
    #
    # 构造规则（确定性且随 n 增长）：
    #   m = n * (n + 1) // 2 - n // 2
    # 这样 m 介于 1..n(n+1)/2 之间，且随 n 单调增长
    m = n * (n + 1) // 2 - n // 2

    for i in range(1, n + 1):
        j = i * (i + 1) // 2
        if j >= m:
            if j == m and i == n:
                # print(0)
                pass
                break

            else:
                t = n - i
                if j - t == m:
                    # print(t)
                    pass
                    break
                elif j - t < m:
                    continue


if __name__ == "__main__":
    # 示例：使用 n=10 进行一次确定性实验
    main(10)