import random

def main(n):
    # 生成测试数据：
    # n: 总长度
    # pos: [1, n]
    # l, r: 满足 1 <= l <= r <= n
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    x = [n, pos, l, r]

    pos = x[1]
    n = x[0]
    l = x[2]
    r = x[3]
    step = 0

    if pos < l:
        step = l - pos + 1
        if r < n:
            step += r - l + 1
    elif pos > r:
        step = pos - r + 1
        if l > 1:
            step += r - l + 1
    else:
        if l > 1 and n > r:
            step += min(pos - l, r - pos) + r - l + 2
        elif l == 1 and n > r:
            step = r - pos + 1
        elif l > 1 and n == r:
            step += pos - l + 1
        else:
            step = 0

    print(step)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)