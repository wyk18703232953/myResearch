def main(n):
    # 映射规则：
    # n 为原程序中的 n
    # v 为一个确定性函数：v = n // 2 + 1（保证 1 <= v <= n）
    v = n // 2 + 1
    if v < 1:
        v = 1
    if v > n:
        v = n

    cur = 0
    total = 0
    for i in range(n):
        while cur < n - i - 1:
            cur += 1
            total += (i + 1)
            if cur == v:
                break
        cur -= 1
    return total


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    result = main(10)
    # print(result)
    pass