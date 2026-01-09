def main(n: int):
    # 根据 n 生成测试数据 (示例策略)：
    # 尝试让构造有解：优先生成 a=1 或 b=1 的情况
    if n <= 1:
        a, b = 1, 1
    elif n < 4:
        # 对于 2,3，如果 a 或 b 都是 1 且另一个也是 1，能过条件
        a, b = 1, 1

    else:
        # 对于 n>=4，选择 a=1, b=2 这样的可行参数
        a, b = 1, 2

    # 以下为原逻辑，只是用生成的 a,b 替代 input()
    if min(a, b) > 1 or (1 < n < 4 and max(a, b) == 1):
        # print('NO')
        pass
        return

    # print('YES')
    pass
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    # print('\n'.join(''.join(map(str, row)) for row in r))
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)