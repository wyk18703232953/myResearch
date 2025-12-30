import random

def main(n: int):
    """
    n 用作规模参数，用来控制生成的测试数据范围。
    这里约定：
    - 生成 left, right 为 [0, n] 区间内的随机整数
    - 且保证 left <= right
    """
    if n < 0:
        raise ValueError("n 必须为非负整数")

    left = random.randint(0, n)
    right = random.randint(left, n)  # 保证 left <= right

    if left == right:
        print(0)
    else:
        x = 1
        while x <= right:
            x *= 2
        x //= 2
        y = x
        # 注意运算符优先级，保持与原程序语义一致
        while (y > 0 and x <= left) or x > right:
            if x <= left:
                x += y
            else:
                x -= y
            y //= 2
        print(x ^ (x - 1))


if __name__ == "__main__":
    # 示例：以 n = 100 为规模运行一次
    main(100)