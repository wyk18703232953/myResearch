def main(n):
    # 映射规则（确定性、可规模化）：
    # 给定规模 n，构造一个与 n 相关的一组输入：
    #   - N = max(2, n)   图的规模
    #   - a = 1 + (n % max(1, N - 1))
    #   - b = 1 + ((n // 2) % max(1, N - 1))
    #
    # 这样当 n 变化时，(N, a, b) 的组合也随之变化，
    # 可以用于分析算法在不同 N、a、b 下的时间复杂度。
    if n < 2:
        N = 2

    else:
        N = n

    if N - 1 <= 0:
        a = 1
        b = 1

    else:
        a = 1 + (n % (N - 1))
        b = 1 + ((n // 2) % (N - 1))

    from collections import defaultdict

    hash_map = defaultdict(list)  # 保留结构但不参与后续逻辑

    if a == 1 and b == 1:
        if N == 2 or N == 3:
            # print('NO')
            pass
            return

    if a == 1 or b == 1:
        visited = [False] * (N + 1)

        if a > N or b > N:
            # print('NO')
            pass
            return
        # print('YES')
        pass

        l = []
        for _ in range(N):
            z = ['0'] * N
            l.append(z)
        ans = []
        for _ in range(N):
            z = ['0'] * N
            ans.append(z)

        if b == 1:
            for i in range(a - 1, N - 1):
                l[i][i + 1] = '1'
                l[i + 1][i] = '1'

            for row in l:
                # print(''.join(row))
                pass

        else:
            ans = []
            for _ in range(N):
                z = ['0'] * N
                ans.append(z)

            for i in range(b - 1, N - 1):
                l[i][i + 1] = '1'
                l[i + 1][i] = '1'

            for i in range(N):
                for j in range(N):
                    if i != j:
                        if l[i][j] == '1':
                            ans[i][j] = '0'
                        if l[i][j] == '0':
                            ans[i][j] = '1'

            for row in ans:
                # print(''.join(row))
                pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：使用不同规模进行实验
    # 可根据需要修改或在外部多次调用 main(n)
    main(5)