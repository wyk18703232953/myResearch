import random

def main(n: int):
    # 生成测试数据：n个随机整数，这里取区间 [-10, 10] 作为示例
    l1 = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑
    if n % 2 == 0:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1
    else:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1
        idx = l1.index(min(l1))
        l1[idx] = l1[idx] * -1 - 1

    print(' '.join(str(x) for x in l1))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)