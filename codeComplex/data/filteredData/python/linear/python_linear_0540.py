import random

def main(n):
    # 生成测试数据：n 个整数，范围可自行调整
    # 这里设定为 [-10, 10]
    a = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑开始
    if n == 1:
        print(a[0])  # Obvious Case
        return

    sm = 0
    havePositive = False
    haveNegative = False

    for c in a:
        if c == 0:
            haveNegative = True
            havePositive = True
        elif c > 0:
            havePositive = True
            sm += c
        else:
            haveNegative = True
            sm -= c

    if haveNegative and havePositive:
        print(sm)  # Final Answer
    else:
        for i in range(n):
            a[i] = abs(a[i])
        # Get the minimum
        ans = sum(a)
        low = a[0]
        for c in a:
            low = min(low, c)
        # Final Answer
        print(ans - 2 * low)


if __name__ == "__main__":
    # 示例调用：可以在此修改 n 的值
    main(5)