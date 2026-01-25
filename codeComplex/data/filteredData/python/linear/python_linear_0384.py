def main(n):
    # 映射规则：
    # - 原程序的 n 保持为 n
    # - 原程序的 m 取为 n（即有 n 行参数）
    # - 每行的两个整数 a, b 由 i 的简单算术构造生成
    m = n
    arr = []
    for i in range(m):
        a = i + 1                  # 保证随规模增加而线性增长
        b = (i // 2) - (i % 3)     # 可产生正负交替的线性大小
        arr.append([a, b])

    count = 0
    for i in range(m):
        count += arr[i][0] * n
        if n % 2 == 1 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 + 1) * arr[i][1]
        if n % 2 == 1 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2
        if n % 2 == 0 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 - 1) * arr[i][1]
            count += (n // 2) * arr[i][1]
        if n % 2 == 0 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2
    result = count / n
    print(result)
    return result


if __name__ == "__main__":
    # 示例：用若干不同规模运行以便做时间复杂度实验
    for size in [10, 100, 1000]:
        main(size)