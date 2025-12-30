import random

def main(n):
    # 生成测试数据：构造一个满足条件的 vals，然后据此反推 l 和 r
    # 1. 随机生成 vals（1..n 的值，允许重复）
    vals = [random.randint(1, n) for _ in range(n)]

    # 2. 根据 vals 计算 l 和 r
    l = []
    r = []
    for i in range(n):
        li = sum(1 for x in vals[:i] if x > vals[i])
        ri = sum(1 for x in vals[i:] if x > vals[i])
        l.append(li)
        r.append(ri)

    # 以下是原逻辑（去掉 input，改用生成的 l, r）
    items = [(-l[i] - r[i], i) for i in range(n)]
    items.sort()
    ans_vals = [1] * n
    m = 1
    for i in range(1, n):
        if items[i - 1][0] != items[i][0]:
            m += 1
        ans_vals[items[i][1]] = m

    for i in range(n):
        ln = sum(map(lambda x: x - ans_vals[i] > 0, ans_vals[:i]))
        lr = sum(map(lambda x: x - ans_vals[i] > 0, ans_vals[i:]))
        if ln != l[i] or lr != r[i]:
            print('NO')
            break
    else:
        print('YES')
        print(' '.join(str(i) for i in ans_vals))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)