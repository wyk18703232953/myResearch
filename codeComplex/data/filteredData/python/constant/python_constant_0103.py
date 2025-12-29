import random

def max1(a, b):
    if a >= b:
        return a, b
    else:
        return b, a

def minus(a, b):
    p = a // b
    cnt = p
    return b, (a - (b * cnt)), cnt

def main(n):
    """
    n: 测试用例规模（即生成 n 组 (a, b) 数据）
    功能：随机生成 n 组正整数 (a, b)，并对每组执行原逻辑，打印结果。
    """
    # 生成并处理 n 组测试数据
    for _ in range(n):
        # 生成测试数据，范围可根据需要调整
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)

        cnt = 0
        x, y = a, b  # 保留原始数据如有调试需要

        while x > 0 and y > 0:
            x, y = max1(x, y)
            x, y, p = minus(x, y)
            cnt += p

        print(cnt)

if __name__ == "__main__":
    # 示例：调用 main(5) 生成并处理 5 组测试数据
    main(5)