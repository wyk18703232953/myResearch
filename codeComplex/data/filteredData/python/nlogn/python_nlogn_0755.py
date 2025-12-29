def main(n):
    import random

    # 生成测试数据：随机生成一组长度为 n 的整数数组
    # 为确保有意义的结果，n 至少为 2
    if n < 2:
        raise ValueError("n must be at least 2")

    # 生成 a：元素范围可自行调整，这里用 1 ~ 10^9
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 以下为原逻辑的封装
    a.sort()
    result = min(len(a) - 2, a[-2] - 1)
    print(result)


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(5)