import random

def main(n):
    # 随机生成一组合法的 (n, pos, l, r) 测试数据
    # n: 规模，由调用者给定
    # 约束：1 <= l <= r <= n, 1 <= pos <= n
    if n < 1:
        raise ValueError("n must be >= 1")

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
    return step

if __name__ == "__main__":
    # 示例：调用 main(10)，规模为 10
    main(10)