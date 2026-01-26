def main(n):
    # n 表示成对元素的数量，数组长度为 2n
    if n <= 0:
        # print(0)
        pass
        return

    # 构造确定性数组：每个数字 i 出现两次，按顺序排列
    pairs = []
    for i in range(1, n + 1):
        pairs.append(i)
        pairs.append(i)

    N = len(pairs)
    N //= 2
    visited = [False] * (N + 1)

    minimumSwaps = 0

    for i in range(2 * N):
        if visited[pairs[i]] is False:
            visited[pairs[i]] = True
            count = 0
            for j in range(i + 1, 2 * N):
                if visited[pairs[j]] is False:
                    count += 1
                elif pairs[i] == pairs[j]:
                    minimumSwaps += count
    # print(minimumSwaps)
    pass
if __name__ == "__main__":
    main(10)