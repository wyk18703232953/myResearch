def main(n):
    # 生成测试数据：
    # 设 k 固定为 3，m = n
    # 生成 n 个递增的正整数作为 L（模拟原题中已排序的下标或编号）
    k = 3
    m = n
    # 简单生成：L[i] = (i+1)*2，保证递增且较稀疏
    L = [(i + 1) * 2 for i in range(m)]

    # 原逻辑开始
    off = 1
    page = -1
    c = 0
    ans = 0
    for l in L:
        p = (l - off) // k
        if p == page:
            c += 1
        else:
            off += c
            c = 1
            ans += 1
            page = (l - off) // k

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)