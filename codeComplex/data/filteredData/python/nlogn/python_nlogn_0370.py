def main(n):
    # 映射含义：
    # n: 数组长度
    # k: 按固定规则从 n 导出，保证确定性且可随规模变化
    k = n // 3  # 可根据需要调整规模关系

    # 确定性生成测试数据 a，长度为 n
    # 示例：a[i] = (i * 2) % (n + 5)
    a = [(i * 2) % (n + 5) for i in range(n)]

    # 核心算法逻辑保持不变
    a.sort()
    slow, fast = 0, 0
    while fast < n:
        if a[slow] == a[fast]:
            fast += 1
        elif abs(a[slow] - a[fast]) <= k:
            a[slow] = 0
            slow += 1

        else:
            slow += 1
            if slow > fast:
                fast = slow
    ans = 0
    for i in a:
        if i != 0:
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)