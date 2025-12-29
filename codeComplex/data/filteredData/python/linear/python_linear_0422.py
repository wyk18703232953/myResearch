import random
from collections import Counter

def main(n):
    # 生成测试数据
    # n: 数组长度
    # x: 与运算的掩码，这里取一个与数组元素同数量级的随机数
    max_val = max(1, n * 2)
    x = random.randint(1, max_val)
    a = [random.randint(1, max_val) for _ in range(n)]

    # 输出生成的测试数据（如不需要可以去掉这两行）
    print("n x:", n, x)
    print("a:", *a)

    # 原逻辑开始
    d = Counter(a)
    sa = set(a)
    if len(sa) < n:
        print(0)
    else:
        c = 0
        for i in a:
            k = i & x
            if k != i and k in d:
                c = 1
                print(1)
                break
        if c == 0:
            z = []
            for i in a:
                z.append(i & x)
            if len(set(z)) < n:
                print(2)
            else:
                print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)