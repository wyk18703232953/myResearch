from collections import namedtuple
import random

vertex = namedtuple('vertex', ['degree', 'id'])


def main(n):
    # 生成测试数据 rr：长度为 n 的度数序列，保证和至少为 2*(n-1)，且大于 0
    # 简单策略：先给每个点度数为 1，然后在前若干个点上随机加一些度数
    rr = [1] * n
    extra = max(0, 2 * (n - 1) - sum(rr))  # 至少需要的额外度数
    # 再随机增加一些度，使情况更丰富
    extra += random.randint(0, n)

    for _ in range(extra):
        idx = random.randrange(n)
        rr[idx] += 1

    a, b, c = [], [], 0

    for i in range(n):
        if rr[i] > 1:
            a.append(vertex(rr[i], i + 1))
        else:
            b.append(vertex(rr[i], i + 1))
        c += rr[i]

    if c < (n - 1) * 2:
        print('NO')
        return

    print('YES', len(a) - 1 + min(2, len(b)))
    print(n - 1)
    for i in range(1, len(a)):
        print(a[i - 1].id, a[i].id)
    if len(b) > 0:
        print(b[0].id, a[0].id)
    if len(b) > 1:
        print(b[1].id, a[-1].id)
    j, yes = 2, 0
    for i in range(len(a)):
        k = a[i].degree - 2
        for _ in range(k):
            if j >= len(b):
                yes = 1
                break
            print(a[i].id, b[j].id)
            j += 1
        if yes == 1:
            break


if __name__ == "__main__":
    # 示例调用：n 可以按需修改
    main(5)