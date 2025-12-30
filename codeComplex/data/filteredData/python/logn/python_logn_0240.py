def main(n):
    # 随机/规则生成规模为 n 的测试数据：
    # 原程序中有两个输入：n, s
    # 这里保持 n 为参数，将 s 作为 n 的函数来生成测试数据。
    # 可根据需要调整生成规则，这里示例设为：s = n // 2
    s = n // 2

    ok, ng = 10**18 + 100, -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        if mid - sum(map(int, str(mid))) >= s:
            ok = mid
        else:
            ng = mid

    # 原逻辑输出
    ans = max(0, n - ok + 1)
    print(ans)


if __name__ == "__main__":
    # 示例：运行 main(10**12) 或其他规模
    main(10**12)