from collections import defaultdict as dd
import random

def main(n):
    # 生成测试数据：长度为 n 的数组，元素为 1..max(4, n//2) 之间的随机整数
    max_val = max(4, n // 2)
    l = [random.randint(1, max_val) for _ in range(n)]

    l1 = dd(int)
    a = 0
    for j in l:
        l1[j] += 1
        if l1[j] == 4:
            a = j
    if a:
        print(a, a, a, a)
    else:
        c = 0
        x = 0
        l2 = []
        for j in l1:
            if l1[j] >= 2:
                l2.append(j)
        l2.sort()
        a = b = 0
        for j in l2:
            c += 1
            if c == 1:
                a = j
            elif c == 2:
                b = j
            else:
                if x / j + j / x < a / b + b / a:
                    a, b = x, j
            x = j
        print(a, a, b, b)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)