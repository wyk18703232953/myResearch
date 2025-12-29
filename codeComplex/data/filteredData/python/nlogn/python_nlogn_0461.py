import random

def main(n):
    # 规模参数：n，需满足 n >= 1
    # 这里示例令 k 为 [1, n] 间的随机值
    k = random.randint(1, n)

    # 生成测试数据 a：长度为 n 的随机整数数组
    # 元素范围可按需求调整，这里设置为 [1, 10^9]
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 以下为原逻辑改写，无 input()
    b = list(a)
    b.sort()
    c = []
    total = 0
    for i in range(1, k + 1):
        c.append(b[-i])
        total += b[-i]
    print(total)

    d = []
    tmp = list(c)  # 防止直接修改 c 时干扰后续逻辑的理解
    for i in range(n):
        if a[i] in tmp:
            d.append(i)
            tmp.remove(a[i])
    d.insert(0, -1)
    d[-1] = n - 1
    e = []
    for i in range(1, len(d)):
        e.append(d[i] - d[i - 1])
    print(" ".join(map(str, e)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)