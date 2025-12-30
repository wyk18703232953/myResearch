import random

def main(n: int) -> None:
    # 生成规模为 n 的测试数据：随机整数列表
    # 这里假设元素为 1~n 的随机排列，如需其他分布可自行调整
    t = list(range(1, n + 1))
    random.shuffle(t)

    sw = 0
    # 按原逻辑处理列表 t
    while t != []:
        # pr 是 t[0] 在 t[1:] 中第一次出现的位置（1-based，再加 1）
        pr = 1 + t[1:].index(t[0])
        sw += pr - 1
        # 删除 t[0] 和 t[pr] 中间的元素
        t = t[1:pr] + t[pr+1:]

    print(sw)


if __name__ == "__main__":
    # 示例：运行时可在此调整 n 的值
    main(10)