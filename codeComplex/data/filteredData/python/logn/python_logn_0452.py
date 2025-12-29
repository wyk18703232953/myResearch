max_ = 10**18
arr  = [0, 1]
arr2 = [0, 3]

# 预处理，与原逻辑一致
while arr[-1] < max_:
    arr.append(arr[-1] * 4)
    arr2.append(arr2[-1] * 2 + 1)

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]


def solve(n, k):
    if n == 2 and k == 3:
        return 'NO'
    if n == 2 and k == 4:
        return 'YES 0'
    if n + 1 <= len(arr) and k > arr[n]:
        return 'NO'

    i = 0
    while k >= arr[i + 1]:
        i += 1
    if k - arr[i] > arr2[i]:
        i += 1
    return 'YES ' + str(n - i)


def main(n):
    """
    参数 n 为测试数据规模。
    这里根据 n 生成 n 组 (n_i, k_i) 测试数据：
      n_i: 从 2 到 n+1
      k_i: 取一个与 n_i 相关的值（这里简单使用 n_i^2 作为示例）
    可根据需要修改生成策略。
    """
    results = []
    for i in range(1, n + 1):
        ni = i + 1            # 保证 n_i >= 2
        ki = ni * ni          # 示例测试数据，可自行调整生成方式
        results.append(solve(ni, ki))
    # 输出结果（与原程序表现一致）
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：当需要测试规模为 5 时调用 main(5)
    main(5)