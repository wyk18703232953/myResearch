def main(n):
    # 这里假设 k 按比例生成，例如取 n 的一半（可按需要调整生成规则）
    k = n // 2

    ans = ""
    # 原逻辑：每次拼接 (n - k) // 2 个 '1' 再拼接一个 '0'
    block_ones = (n - k) // 2
    if block_ones <= 0:
        # 如果 block_ones 不为正，原程序会陷入死循环；
        # 这里做保护：直接输出前 n 个 '0'
        ans = '0' * n
    else:
        while len(ans) < n:
            ans += '1' * block_ones + '0'
        ans = ans[:n]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改规模 n
    main(10)