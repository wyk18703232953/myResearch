import random

def main(n):
    # 生成测试数据
    # m 为初始值，正数
    m = random.randint(1, 1000)
    # a, b 为长度为 n 的数组，元素在 [1, 10] 内随机生成
    a = [random.randint(1, 10) for _ in range(n)]
    b = [random.randint(1, 10) for _ in range(n)]

    curr = float(m)
    f = 0

    if b[0] != 1:
        curr += curr / (b[0] - 1)
    else:
        f = 1

    for i in range(n - 1, -1, -1):
        if a[i] != 1:
            curr += curr / (a[i] - 1)
        else:
            f = 1
        if i > 0:
            if b[i] != 1:
                curr += curr / (b[i] - 1)
            else:
                f = 1

    if f:
        print(-1)
    else:
        print(curr - m)


if __name__ == "__main__":
    # 示例调用：规模 n = 5
    main(5)