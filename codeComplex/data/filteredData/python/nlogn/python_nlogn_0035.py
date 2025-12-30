import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里示例为在 [1, 10] 内随机生成 n 个整数
    a = [random.randint(1, 10) for _ in range(n)]

    # 2. 按原逻辑处理
    a = sorted(a)
    if a[-1] == 1:
        result = [*a[:-1], 2]
    else:
        result = [1, *a[:-1]]

    # 3. 输出结果
    print(*result)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(5)