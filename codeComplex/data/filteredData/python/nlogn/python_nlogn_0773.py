import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据 a
    # 这里示例生成 1 到 10^9 之间的随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑
    idx = list(range(n))
    idx.sort(key=lambda i: a[i], reverse=True)
    imin = imax = idx[0]
    for i in idx[1:]:
        if i == imin - 1 or i == imax + 1:
            imin = min(imin, i)
            imax = max(imax, i)
        else:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    # 示例：可在此处修改 n 进行测试
    main(10)