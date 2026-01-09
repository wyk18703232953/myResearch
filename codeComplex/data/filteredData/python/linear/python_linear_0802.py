def main(n):
    # 映射 n 为原程序的 n, m, k 和数组 pi 的规模
    # 这里令：
    #   m = n
    #   k = max(1, n // 10)  保证 k 不为 0 且随规模变化
    #   n_val = n * 10       原始意义上的 n（足够大，能覆盖所有 pi）
    m = n
    k = max(1, n // 10)
    n_val = n * 10

    # 构造确定性的 pi：长度为 m，值在 [1, n_val] 内递增
    # pi[i] = (i+1)*2，且不超过 n_val
    pi = [min((i + 1) * 2, n_val) for i in range(m)]

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

    return ans


if __name__ == "__main__":
    # 示例：调用 main，规模可按需修改
    result = main(1000)
    # print(result)
    pass