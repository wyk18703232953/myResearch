def main(n):
    # 对于原程序：n, k = minput()
    # 这里将输入规模参数 n 作为原来的第一个输入
    # 第二个输入 k 可确定性构造为 n // 2
    total_n = n
    k = n // 2
    # 核心算法逻辑保持不变
    for i in range(1, total_n + 1):
        if (i * (i + 1)) / 2 - total_n + i == k:
            # print(total_n - i)
            pass
            break

if __name__ == "__main__":
    main(10)