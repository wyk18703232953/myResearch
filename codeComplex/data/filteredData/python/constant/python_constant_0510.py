import random

def main(n):
    # n 表示查询次数 q
    q = n
    random.seed(0)  # 固定种子，保证复现性

    for _ in range(q):
        # 生成测试数据 (x, y, k)
        # 保证 x, y, k 为非负整数，且规模与 n 相关
        upper = max(1, n * 2)
        x = random.randint(0, upper)
        y = random.randint(0, upper)
        k = random.randint(0, upper)

        if max(x, y) > k:
            print(-1)
        elif x == y and k == x + 1:
            print(k - 2)
            continue
        elif x % 2 == 1 and y % 2 == 1 and k % 2 == 0:
            print(k - 2)
            continue
        elif x % 2 == 0 and y % 2 == 0 and k % 2 == 1:
            print(k - 2)
            continue
        elif (x + y) % 2 == 0:
            print(k)
        else:
            print(k - 1)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)