def main(n):
    # 保证规模合理，至少为 2
    if n < 2:
        n = 2

    # 确定性生成长度为 n 的数组 arr
    # 使用简单算术规则：arr[i] = (i * 7 + 3) % (n + 5)
    arr = [(i * 7 + 3) % (n + 5) for i in range(n)]

    p = n + 7  # 让模数随规模变化，且大于 0

    res = []

    prefsums = [arr[0]]

    for i in range(1, n):
        prefsums.append(prefsums[i - 1] + arr[i])

    allsum = sum(arr)

    if len(arr) == 2:
        print(arr[0] % p + arr[1] % p)
        return

    for i in range(1, n - 1):
        res.append((prefsums[i] % p) + ((allsum - prefsums[i]) % p))

    print(max(res))


if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)