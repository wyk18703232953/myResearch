def main(n: int):
    # 直接使用给定逻辑，将原来的 input() 去掉，封装为 main(n)

    if n == 3:
        print('1 1 3')
        return
    if n == 1:
        print('1')
        return
    if n == 2:
        print('1 2')
        return

    d = 2
    ans = []
    lfn = n
    while d <= n:
        k = n // d
        for _ in range(lfn - k):
            ans.append(d // 2)
        lfn = n - len(ans)
        d *= 2

    d //= 2
    k = n / d
    if k < 1.5:
        ans.append(d)
    else:
        ans.append(d + d // 2)

    print(' '.join(str(i) for i in ans))


# 下面示例：根据 n 自动生成测试数据并调用 main
# 可按需修改或在其他模块中调用 main(n)
if __name__ == "__main__":
    # 示例：生成一个规模为 10 的测试
    test_n = 10
    main(test_n)