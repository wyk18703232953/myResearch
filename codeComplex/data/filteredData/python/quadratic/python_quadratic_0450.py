import random


def main(n: int):
    # 生成测试数据：随机排列 1..n
    a = list(range(1, n + 1))
    random.shuffle(a)

    n2idx = {a[i]: i for i in range(n)}
    f = [False] * (n + 1)

    for i in range(n, 0, -1):
        idx_lg = n2idx[i]
        win_flag = False
        for j in range(idx_lg % i, n, i):
            if a[j] > i and not f[a[j]]:
                win_flag = True
                break
        f[i] = win_flag

    res = ''.join('A' if f[a_i] else 'B' for a_i in a)
    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时请按需修改 n
    main(5)