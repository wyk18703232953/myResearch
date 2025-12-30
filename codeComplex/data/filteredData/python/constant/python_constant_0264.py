import random

def main(n: int):
    # 生成测试数据：
    # n: 1..n
    # pos: 1..n
    # l, r: 1..n 且 l <= r
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    time = 0
    if l != 1 and r != n:
        if abs(pos - l) < abs(pos - r):
            time += abs(pos - l) + abs(l - r) + 2
        else:
            time += abs(pos - r) + abs(l - r) + 2
    elif l == 1 and r != n:
        time += abs(pos - r) + 1
    elif r == n and l != 1:
        time += abs(pos - l) + 1
    else:
        time += 0

    print(time)


if __name__ == '__main__':
    # 示例：以 n=10 运行
    main(10)