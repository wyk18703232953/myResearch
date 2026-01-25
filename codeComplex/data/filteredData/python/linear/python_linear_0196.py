def main(n):
    # 将 n 解释为数组长度，其他参数用固定确定性规则生成
    # 为了保持规模意义清晰：
    #   - 数组长度 = n
    #   - T, a, b, c 随 n 确定性变化，但与随机无关
    if n <= 0:
        return

    # 确定性参数构造（与 n 相关，避免退化为完全常数）
    a = 5 + (n % 7)       # 基础值略随 n 变化
    b = 3 + (n % 5)
    c = 2 + (n % 4)
    # 保证 T 至少为 1，且不大于 n+5 左右的量级
    T = max(1, (n // 3) + 2)

    # 确定性数组生成：arr[j] = (j * 2 + n) % (T + 3)
    # 保证元素大小与 T 有一定关系，避免所有元素都 < T 或都 > T
    arr = [(j * 2 + n) % (T + 3) for j in range(n)]

    Tcnt = arr.count(T)
    l = n - Tcnt  # 未使用的变量，保留结构
    ans = 0
    a1 = 0

    for i in range(1, T):
        for j in range(n):
            if arr[j] <= i:
                a1 += 1
        ans += a1 * c
        a1 = 0

    b1 = 0
    for i in range(n):
        b1 = a - ((T - arr[i]) * b)
        if b1 <= 0:
            ans += b1
        else:
            ans += b1

    ans1 = n * a
    result = max(ans, ans1)
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可以根据需要调整 n 规模
    main(10)