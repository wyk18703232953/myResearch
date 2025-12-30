import random

def m(x, y, k):
    d = min(x, y)
    x -= d
    y -= d
    k -= d

    if k - x - y < 0:
        return -1
    else:
        x += y
        if x % 2 > 0 and k % 2 > 0:
            return d + k - 1
        elif x % 2 > 0:
            return d + k - 1
        elif k % 2 > 0:
            return d + k - 2
        else:
            return d + k

def main(n):
    random.seed(0)
    for _ in range(n):
        # 生成测试数据：x, y, k 为正整数，保证有一定规模
        x = random.randint(1, 10**6)
        y = random.randint(1, 10**6)
        k = random.randint(1, 10**6)
        ans = m(x, y, k)
        print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)