def main(n):
    # n 表示列表长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成测试数据：正整数列表
    # 构造方式：从 1 开始的递增序列，再通过简单算术变换
    l1 = [(i + 1) * (1 + (i % 3)) for i in range(n)]

    ans = 0
    l1.sort()
    visited = [0] * n
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans += 1
        for j in range(i + 1, n):
            if visited[j] == 0 and l1[j] % l1[i] == 0:
                visited[j] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)