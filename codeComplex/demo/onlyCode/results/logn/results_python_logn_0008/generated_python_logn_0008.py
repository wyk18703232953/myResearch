import random

def main(n: int):
    # 生成测试数据：构造两个非负整数 l, r（l <= r），规模由 n 控制
    # 这里令 l, r 的比特长度不超过 n（最大不超过 2^n - 1）
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    bitafter = -1
    for i in range(60, -1, -1):
        if (l & (1 << i)) != (r & (1 << i)):
            bitafter = i
            break

    res = 0
    while bitafter >= 0:
        res += 1 << bitafter
        bitafter -= 1

    print(res)


if __name__ == "__main__":
    # 示例调用：可按需调整 n
    main(10)