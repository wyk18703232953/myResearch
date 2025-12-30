import random

def main(n):
    # 生成测试数据：随机生成一个长度为 n 的数组 a，元素为 1..10^9 之间的整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑
    a.sort()
    # 若 n < 2 时，原逻辑会越界，这里做个保护
    if n < 2:
        result = 0
    else:
        result = min(a[-2] - 1, n - 2)

    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(5)