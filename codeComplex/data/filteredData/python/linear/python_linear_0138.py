import random

def main(n):
    # 生成测试数据：n 个非负整数
    # 这里生成 0 到 n 之间的随机整数，可按需修改分布
    a = [random.randint(0, n) for _ in range(n)]

    b = []
    maxi = 0
    for i in range(n):
        maxi = max(maxi, a[i] + 1)
        b.append(maxi)

    c = []
    count = b[-1]
    for i in range(n - 1, -1, -1):
        if count - 1 >= b[i]:
            count -= 1
            c.append(count)
        else:
            c.append(count)
    c = c[::-1]

    ans = 0
    for i in range(n):
        ans += (c[i] - a[i] - 1)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)