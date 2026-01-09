def main(n):
    """
    规模参数 n：生成长度为 n 的数组 arr，按原逻辑计算并返回 ans。
    这里使用简单的测试数据生成方式：arr[i] = i % 5
    如需其它分布，可自行修改生成方式。
    """
    # 生成测试数据
    arr = [i % 5 for i in range(n)]

    t = [0] * n
    cur = 0
    # 第一段逻辑：从后往前计算 t[i]
    for i in range(n - 1, -1, -1):
        cur = max(cur - 1, 0, arr[i] + 1)
        t[i] = cur

    ans = 0
    # 第二段逻辑：从前往后累加 ans
    for i in range(n):
        cur = max(cur, t[i])
        ans += cur

    # 减去所有 (arr[i] + 1)
    for i in range(n):
        ans -= (arr[i] + 1)

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)