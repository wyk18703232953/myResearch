def main(n):
    # n 表示原程序中的 n，k 由 n 确定性生成
    # 这里将 k 定义为从 1 到 n 的所有可能值依次测试，并输出最后一个结果
    # 若希望单次运行只测试一个 k，也可以改为固定映射，如 k = n // 2 + 1
    last_c = None
    for k in range(1, n + 1):
        i = 0
        t = 0
        while k > i:
            t += 1
            i += t
        c = n - t
        i -= c
        while i != k:
            t += 1
            i += t + 1
            c -= 1
        last_c = c
    return last_c

if __name__ == "__main__":
    # 示例调用：使用 n = 10 作为规模
    result = main(10)
    # print(result)
    pass