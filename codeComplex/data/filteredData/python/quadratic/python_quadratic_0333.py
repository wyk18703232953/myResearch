import random


def solve(n, d, k):
    _min = d + 1

    if n < _min:
        print('NO')
    else:
        res = []
        deg = [0] * (n + 1)
        dist = [0] * (n + 1)

        stack = []
        deg[1] = 1
        for i in range(1, d + 1):
            res.append((i, i + 1))
            if i > 1:
                deg[i] += 2
            dist[i] = max(i - 1, d + 1 - i)
        dist[d + 1] = d
        deg[d + 1] = 1

        for i in range(2, d + 1):
            stack.append(i)

        nxt = d + 2
        while stack:
            if nxt > n:
                break
            v = stack.pop()
            if dist[v] < d:
                while nxt <= n and deg[v] < k:
                    res.append((v, nxt))
                    deg[v] += 1
                    deg[nxt] += 1
                    dist[nxt] = dist[v] + 1
                    if dist[nxt] < d:
                        stack.append(nxt)
                    nxt += 1

        ok = nxt > n
        ok &= all(deg[i] <= k for i in range(1, n + 1))
        ok &= all(dist[i] <= d for i in range(1, n + 1))

        if not ok:
            print('NO')
        else:
            print('YES')
            for e in res:
                print(*e)


def main(n):
    # 根据规模 n 生成测试数据 (n, d, k)
    # 简单策略：让 d 和 k 都在 [1, n] 内随机或按比例生成
    if n < 2:
        # 对于极小规模，构造必然失败的测试以保持逻辑完整
        d = 1
        k = 1
    else:
        # 把直径控制在 [1, max(1, n//2)]
        d = random.randint(1, max(1, n // 2))
        # 度数上界在 [1, n-1]
        k = random.randint(1, max(1, n - 1))

    # 输出本次使用的参数，便于调试（如不需要可删除下一行）
    # print(f'# test params: n={n}, d={d}, k={k}')
    solve(n, d, k)


if __name__ == '__main__':
    # 示例：当作脚本直接运行时，给一个默认规模
    main(10)