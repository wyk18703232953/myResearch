import random

def main(n: int):
    # 生成测试数据：长度固定为 14，与原程序逻辑保持一致
    # 可根据需要调整生成规则
    xs = [random.randint(0, n) for _ in range(14)]

    res = 0
    for i in range(14):
        newxs = xs[:]
        newxs[i] = 0
        base = xs[i] // 14
        rem = xs[i] % 14

        for j in range(14):
            newxs[j] += base

        for j in range(rem):
            newxs[(i + 1 + j) % 14] += 1

        res = max(res, sum(val for val in newxs if val % 2 == 0))

    print(res)


if __name__ == "__main__":
    # 示例：n 用于控制随机数据规模
    main(100)