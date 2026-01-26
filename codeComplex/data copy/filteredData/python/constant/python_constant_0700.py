def main(n):
    # 将 n 作为原程序中的第一个输入，第二个输入 k 由 n 确定性生成
    # 这里设定 k = n // 2，保证 0 <= k <= n
    if n <= 0:
        return  # 对非正规模不做任何输出
    k = n // 2

    if k >= n - 1:
        result = n - 1

    else:
        result = k + ((n - k) * (n - k + 1)) // 2 - 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(10)