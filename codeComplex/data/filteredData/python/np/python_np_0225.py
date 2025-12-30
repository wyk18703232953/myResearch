from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # l, r, x 的范围以及 a 中元素的范围可根据需要调整
    # 这里给出一种合理的随机生成方式
    a = [random.randint(1, 100) for _ in range(n)]
    l = random.randint(1, 50)
    r = random.randint(l, 150)
    x = random.randint(0, 50)

    c = 0
    for i in range(1, n + 1):
        for j in combinations(a, i):
            if l <= sum(j) <= r and max(j) - min(j) >= x:
                c += 1

    print(c)
    return c

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)