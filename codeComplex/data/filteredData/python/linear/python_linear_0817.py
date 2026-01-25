def main(n):
    # 将 n 映射为原程序中的 (n, k)
    # 这里选择 k 为一个确定性的二次函数，保证随规模变化
    N = n
    K = n * n + n

    ans = None
    for x in range(1, N + 1):
        if x * (x + 3) == 2 * (K + N):
            ans = N - x
            break
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模化实验
    main(10)