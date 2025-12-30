import random

def main(n: int):
    # 生成测试数据：a 为 1..n 的随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    rev = [-1] * (n + 1)
    for i, j in enumerate(a):
        rev[j] = i

    mx = max(a)

    # [l, r]
    l = a.index(mx)
    r = l

    for i in range(n - 1, 0, -1):
        idx = rev[i]
        if idx == l - 1:
            l -= 1
        elif idx == r + 1:
            r += 1
        else:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)