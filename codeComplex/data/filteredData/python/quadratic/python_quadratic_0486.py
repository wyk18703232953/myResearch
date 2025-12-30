import random

def lr(a):
    l = [0] * len(a)
    r = [0] * len(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] > a[i]:
                r[i] += 1
            if a[i] > a[j]:
                l[j] += 1
    return l, r


def main(n):
    # 生成一个 1..n 的随机排列作为测试数据
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 根据生成的 a 计算对应的 l, r
    l, r = lr(a)

    # 按原逻辑尝试从 l, r 还原 a
    a_rec = [0] * n
    for i in range(n):
        for j in range(n):
            if l[j] + r[j] == i:
                a_rec[j] = n - i

    l1, r1 = lr(a_rec)
    if l1 != l or r1 != r:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in a_rec))


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)