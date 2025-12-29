import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里设定字符串长度为 n，保证 b 的长度不小于 a
    # 可根据需要调整长度关系
    al = n
    bl = n + random.randint(0, n)  # 至少和 a 一样长，可更长

    # 随机生成只含 '0' 和 '1' 的字符串 a, b
    a = ''.join(random.choice('01') for _ in range(al))
    b = ''.join(random.choice('01') for _ in range(bl))

    count = 0
    al = len(a)
    bl = len(b)

    # 原逻辑
    s = b[:bl - al + 1].count('1')
    for i in range(al - 1):
        if a[i] == '0':
            count += s
        else:
            count += bl - al + 1 - s
        s += int(b[bl - al + i + 1]) - int(b[i])

    if a[-1] == '0':
        count += s
    else:
        count += bl - al + 1 - s

    print(count)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)