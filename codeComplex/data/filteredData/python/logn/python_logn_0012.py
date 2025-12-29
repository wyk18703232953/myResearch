import random

def main(n: int):
    # 生成测试数据：随机生成 0 <= l <= r < 2^n
    if n <= 0:
        return

    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)

    x = n - 1
    while x >= 0 and (l & (1 << x)) == (r & (1 << x)):
        x -= 1

    if x < 0:
        ans = 0
    else:
        ans = (1 << (x + 1)) - 1

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 64 的规模
    main(64)