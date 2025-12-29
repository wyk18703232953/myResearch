import random

def main(n):
    # 生成规模为 n 的测试数据
    Q = n
    # 这里生成随机测试数据，你可根据需要修改数据范围
    src = []
    for _ in range(Q):
        x = random.randint(0, 10**6)
        y = random.randint(0, 10**6)
        k = random.randint(0, 10**6)
        src.append((x, y, k))

    ans = []
    for x, y, k in src:
        d = max(x, y)
        if (x + y) % 2:
            ans.append(-1 if d > k else k - 1)
        else:
            if d > k:
                ans.append(-1)
            else:
                ans.append(k - 2 if (d + k) % 2 else k)

    print(*ans, sep='\n')


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)