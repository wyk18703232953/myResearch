def main(n):
    # 对于原程序，输入为单组：n, m, k, l
    # 这里将 n 作为原来的 n，其他参数按确定性规则生成
    # 确保 m > 0
    m = n // 3 + 1
    k = n // 2
    l = n // 4

    if (l + k) % m == 0:
        c = (l + k) // m

    else:
        c = (l + k) // m + 1
    if m * c > n:
        # print(-1)
        pass

    else:
        # print(c)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模实验
    main(10)