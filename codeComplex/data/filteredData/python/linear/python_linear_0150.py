def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成数组 arr：简单等差序列，从 1 到 n
    arr = [i for i in range(1, n + 1)]

    p = n + 10  # 确定性生成模数 p，随规模增长

    res = []

    prefsums = [arr[0]]

    for i in range(1, n):
        prefsums.append(prefsums[i - 1] + arr[i])

    allsum = sum(arr)

    if len(arr) == 2:
        # print(arr[0] % p + arr[1] % p)
        pass
        return

    for i in range(1, n - 1):
        res.append((prefsums[i] % p) + ((allsum - prefsums[i]) % p))

    # print(max(res))
    pass
if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次规模为 10 的实验
    main(10)