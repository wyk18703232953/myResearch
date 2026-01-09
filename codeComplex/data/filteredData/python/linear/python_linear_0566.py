def main(n):
    if n <= 0:
        return

    # 构造一个确定性的排列 pi，长度为 n-1（和原程序一致）
    # 例如：pi[i] = (i*2 + 1) % n，确保在 [0, n-1] 内
    if n == 1:
        # print(1)
        pass
        return

    pi = [((i * 2 + 1) % n) for i in range(n - 1)]

    ai = [1] * (n + 1)
    ai[0] = 10**9
    for i in pi:
        ai[i] = 0
    for i in range(n - 2, -1, -1):
        ai[pi[i]] += ai[i + 2]
    ai.sort()
    for i in range(n):
        # print(ai[i], end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 进行规模实验
    main(10)