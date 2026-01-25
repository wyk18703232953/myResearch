def main(n):
    # 映射：原程序有两个输入 n, k
    # 这里将 k 作为 n 的确定性函数生成，例如 k = n // 2
    k = n // 2

    # 保持原有算法逻辑不变
    for puts in range(10**9):
        candy = puts * (puts + 1) // 2
        if candy - (n - puts) == k:
            print(n - puts)
            return

if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(1000)