def main(n):
    # 映射：n 为元素个数 m，同时构造 k 和 pi
    m = max(1, n)
    k = max(1, n // 3)  # 保证 k 不为 0，且随规模增长
    # 生成严格递增的 pi，模拟原输入
    # pi[i] 从 1 开始递增，每次增加 1 或 2，完全确定性
    pi = [i + 1 + (i // 2) for i in range(m)]

    num = 1
    ans = 0
    i = 0
    while i < m:
        temp = (pi[i] - num) // k
        temp2 = i
        i += 1
        while i < m:
            if temp != (pi[i] - num) // k:
                break
            i += 1
        num += (i - temp2)
        ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以按需修改 n
    main(1000)