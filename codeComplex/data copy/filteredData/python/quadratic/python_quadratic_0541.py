def main(n):
    # 生成确定性输入：n，和长度为 n 的序列 a[1..n]
    # 保证与原程序逻辑相容：sum(a[i]) >= 2*(n-1) 才有可能形成树的度序列
    # 这里构造一个固定模式：前若干个点度较大，后面大量度为 1
    if n <= 0:
        return

    a = [0]
    if n == 1:
        a.append(0)

    else:
        # 构造度序列：
        # 前 k 个点度较大，其余尽量为 1，使 sum(a) 接近 2*(n-1)
        # 这是完全确定的算术构造
        target_sum = 2 * (n - 1)
        base = [2 + (i % 3) for i in range(1, min(n, 5) + 1)]  # 2,3,4,2,3...
        a.extend(base)
        while len(a) < n + 1:
            a.append(1)
        current_sum = sum(a[1:])
        # 调整总和到不小于 target_sum
        idx = 1
        while current_sum < target_sum and idx <= n:
            a[idx] += 1
            current_sum += 1
            idx += 1
            if idx > n:
                idx = 1
        # 如果总和太大，稍微回退
        idx = n
        while current_sum > target_sum and idx >= 1:
            if a[idx] > 1:
                a[idx] -= 1
                current_sum -= 1
            idx -= 1

    edge = []
    last = 0
    total_sum = 0
    ans = 0

    for i in range(1, n + 1):
        total_sum += a[i]

    for i in range(1, n + 1):
        if a[i] == 1:
            last = i
    if last != 0:
        a[last] = 0

    for i in range(1, n + 1):
        if a[i] > 1:
            if last:
                edge.append([last, i])
                ans += 1
            last = i

    for i in range(1, n + 1):
        if a[i] == 1 and last:
            edge.append([last, i])
            last = 0
            a[i] = 0
            ans += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[j] == 1 and a[i] > 2:
                edge.append([i, j])
                a[i] -= 1
                a[j] -= 1

    if len(edge) != n - 1:
        # print("NO")
        pass

    else:
        # print("YES", ans)
        pass
        # print(len(edge))
        pass
        for u, v in edge:
            # print(u, v)
            pass
if __name__ == "__main__":
    # 示例：对若干规模运行，以便做时间复杂度实验
    for size in [5, 10, 50]:
        # print("---- n =", size, "----")
        pass
        main(size)