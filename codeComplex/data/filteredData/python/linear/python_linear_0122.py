import random

def main(n: int):
    # 生成测试数据：构造一个长度为 n 的父节点数组 a[1..n]
    # 保证对于每个 i >= 2，a[i] 是 [1, n] 中的一个整数
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = random.randint(1, n)

    b = [0] * (n + 1)
    c = [0] * (n + 1)

    for i in range(2, n + 1):
        b[a[i]] += 1

    for i in range(1, n + 1):
        if b[i] == 0:
            c[a[i]] += 1

    for i in range(1, n + 1):
        if b[i] != 0 and c[i] < 3:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)