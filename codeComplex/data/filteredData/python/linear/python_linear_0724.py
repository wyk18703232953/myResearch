import random

def main(n):
    # 生成规模为 n 的测试数据
    # 设置 b 的长度为 n, g 的长度为 n 或 n+1 保证可运行
    m = n  # 这里以 m = n 为例
    # 可以调整随机范围以满足需要
    b = [random.randint(1, 10**9) for _ in range(n)]
    g = [random.randint(1, 10**9) for _ in range(m)]

    result = 0

    bMax, bMax2, bSum = -1, -1, 0
    for bb in b:
        bSum += bb
        if bb > bMax:
            bMax2, bMax = bMax, bb
        elif bb > bMax2:
            bMax2 = bb

    gMin, gSum = float('inf'), 0
    for gg in g:
        gSum += gg
        if gg < gMin:
            gMin = gg

    if bMax > gMin:
        result = -1
    else:
        result = bSum * m
        result += gSum
        result -= bMax * m
        if gMin > bMax:
            result += bMax - bMax2

    print(result)


if __name__ == "__main__":
    # 示例调用：n 为规模
    main(5)