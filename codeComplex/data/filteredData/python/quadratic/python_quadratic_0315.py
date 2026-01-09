def main(n):
    # 映射：原程序有两个输入 n, k 和一个长度为 n 的数组
    # 在实验中，外层 n 作为数组长度，k 取一个与 n 相关的确定性值
    if n <= 0:
        return 0.0

    N = n
    # 选择 k 为 N//2（至少为 1，且不超过 N）
    k = max(1, N // 2)

    # 构造确定性数组 li，长度为 N
    li = [i % 10 for i in range(N)]

    ans = []
    for i in range(0, N):
        su = 0
        for j in range(i, N):
            su += li[j]
            if (j - i + 1 >= k):
                ans.append(su / (j - i + 1))
    res = max(ans) if ans else 0.0
    # print(res)
    pass
    return res


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以测试不同规模
    main(1000)