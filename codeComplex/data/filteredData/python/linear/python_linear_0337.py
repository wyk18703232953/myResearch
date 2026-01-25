def main(n):
    # n 表示数组长度规模，至少为 2
    t = max(2, n)
    d = 1  # 固定间隔参数，保持确定性

    # 构造一个长度为 t 的确定性整数数组
    # 使用简单算术关系 i, i//2 来生成
    arr = [(i * 3 + i // 2) for i in range(t)]

    count = 0
    for i in range(t - 1):
        if arr[i + 1] - arr[i] == 2 * d:
            count += 1
        elif arr[i + 1] - arr[i] > 2 * d:
            count += 2
    result = count + 2
    print(result)
    return result


if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模进行一次运行
    main(10)