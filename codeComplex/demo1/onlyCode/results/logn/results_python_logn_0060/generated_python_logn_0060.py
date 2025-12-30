import random

def main(n: int):
    # 生成测试数据：根据 n 的大小范围生成 l, r
    # 这里使用 [0, 2^n - 1] 范围内的随机数，且保证 l <= r
    if n <= 0:
        l, r = 0, 0
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)

    # 原逻辑
    ans = 0
    for i in range(63, -1, -1):
        if (r & (1 << i)) > 0 and (l & (1 << i)) == 0:
            ans = (1 << (i + 1)) - 1
            break

    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)