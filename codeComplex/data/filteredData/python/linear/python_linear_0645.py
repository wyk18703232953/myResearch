from collections import namedtuple
import random

def main(n):
    # 生成测试数据：一个长度为 n 的度数序列 rr（正整数）
    # 为了更高概率满足生成条件，这里让度数在 [1, n] 范围内
    rr = [random.randint(1, n) for _ in range(n)]

    vertex = namedtuple('vertex', ['degree', 'id'])
    a, b, c = [], [], 0

    for i in range(n):
        tmp = rr[i]
        v = vertex(tmp, i + 1)
        if tmp > 1:
            a.append(v)
        else:
            b.append(v)
        c += tmp

    if c < (n - 1) * 2:
        print('NO')
    else:
        if len(a) == 0:
            print('YES 1')
            print('1 2')
        else:
            print('YES', len(a) - 1 + min(2, len(b)))
            print(n - 1)
            for i in range(len(a)):
                if i == 0:
                    continue
                print(a[i - 1].id, a[i].id)
            if len(b) > 0:
                print(b[0].id, a[0].id)
            if len(b) > 1:
                print(b[1].id, a[-1].id)
            j = 2
            for i in range(len(a)):
                if j >= len(b):
                    yes = 1
                    break
                k = a[i].degree - 2
                yes = 0
                for t in range(k):
                    print(a[i].id, b[j].id)
                    j += 1
                    if j >= len(b):
                        yes = 1
                        break
                if yes == 1:
                    break


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)