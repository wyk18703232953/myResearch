m = 10**18

# 预计算 cc，与原程序一致
cc = [0, 1]
for i in range(2, 50):
    cc.append(min(m, 1 + 4 * cc[-1]))


def run(n, k):
    currn, currs = 1, n
    rem = 0

    while True:
        if k == 0:
            return f'YES {currs}'
        if k < currn or currs == 0:
            return 'NO'
        currs -= 1
        k -= currn
        if currs >= 40:
            rem = m
        else:
            rem = min(m, rem + cc[currs] * ((currn - 1) * 2 + 1))
        currn = (currn - 1) * 2 + 3

        if k <= rem:
            return f'YES {currs}'


def main(n):
    """
    n 为规模参数：
    - 测试次数 t = n
    - 对于第 i 个测试：
        n_i = i + 1
        k_i = i * i
    """
    t = n
    results = []
    for i in range(1, t + 1):
        n_i = i + 1          # 保证 n_i >= 2
        k_i = i * i          # 简单的可重复生成的测试数据
        res = run(n_i, k_i)
        results.append(res)
    # 输出所有结果，每行一个
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行 5 组测试
    main(5)