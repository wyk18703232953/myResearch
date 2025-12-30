import random

def main(n: int):
    # 生成测试数据：l 为 1..n 的随机排列
    l = list(range(1, n + 1))
    random.shuffle(l)

    p = [0] * n
    for i in range(n):
        p[l[i] - 1] = i

    res = ['?'] * n

    for e in range(n, 0, -1):
        i = p[e - 1]
        res[i] = 'B'
        for j in range(i % e, n, e):
            if i != j and l[i] <= l[j] and res[j] == 'B':
                res[i] = 'A'
                break

    print(''.join(res))


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)