import random

def main(n):
    # 随机生成 k，1 <= k <= n
    k = random.randint(1, n)

    # 生成 n 对 (a, b)
    # 这里生成范围可根据需要调整
    lst = []
    for _ in range(n):
        a = random.randint(-10**6, 10**6)
        b = random.randint(-10**6, 10**6)
        lst.append([-a, b])

    lst.sort()
    print(lst.count(lst[k - 1]))


if __name__ == "__main__":
    # 示例：将规模设为 10，可根据需要修改
    main(10)