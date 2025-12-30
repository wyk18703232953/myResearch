import random

def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组 A
    # 示例策略：元素在 [1, 3] 区间内随机生成
    A = [random.randint(1, 3) for _ in range(n)]

    # 与原程序一致：对 A 排序
    A.sort()

    # 核心逻辑
    if A == [1] * n:
        # 全是 1，则输出前 n-1 个 1，再输出一个 2
        res = A[:n-1] + [2]
    else:
        # 否则在最前面补一个 1，去掉原来的最后一个数
        res = [1] + A[:-1]

    # 输出结果
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    # 示例运行：n = 5，可按需修改
    main(5)