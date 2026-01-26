def main(n):
    # 映射：原程序中 n 为输出长度，这里保持不变
    # 需要同时确定 k，设为 n // 2（当 n 为 0 或 1 时特殊处理）
    if n <= 1:
        k = 0

    else:
        k = n // 2

    ans = ""
    # 原逻辑：每次拼接固定数量的 '1'，直到长度达到或超过 n
    while len(ans) < n:
        ans += '1' * ((n - k) // 2) + '0'
    ans = ans[:n]
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的值
    main(10)